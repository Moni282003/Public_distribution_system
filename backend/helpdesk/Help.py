from flask import Flask, request, jsonify
import psycopg2
from sentence_transformers import SentenceTransformer, util
from functools import lru_cache
from datetime import datetime
import ast
import numpy as np


app = Flask(__name__)

DB_CONFIG = {
    "dbname": "kms",
    "user": "postgres",
    "password": "123456",
    "host": "localhost",
    "port": "5432",
}

MODEL = SentenceTransformer("all-MiniLM-L12-v2")

@lru_cache(maxsize=1000)
def get_embedding(question):
    """Generate and cache embeddings for a given question."""
    return MODEL.encode(question)

def connect_db():
    """Establish a connection to the database."""
    return psycopg2.connect(**DB_CONFIG)

def store_question_with_embedding(citizen_id, question):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT query_id FROM helpdesk WHERE question = %s", (question,))
    existing_question = cursor.fetchone()

    if existing_question:
        print(f"Question already exists with Query ID: {existing_question[0]}. No need to store again.")
    else:
        question_embedding = get_embedding(question)
        cursor.execute(
            "INSERT INTO helpdesk (question, asked_by) VALUES (%s, %s) RETURNING query_id",
            (question, citizen_id)
        )
        query_id = cursor.fetchone()[0]
        cursor.execute(
            "INSERT INTO query_embeddings (query_id, embedding) VALUES (%s, %s)",
            (query_id, question_embedding.tolist())
        )
        conn.commit()
        print(f"Your question has been recorded with Query ID: {query_id}. Please wait for an admin to respond.")
    cursor.close()
    conn.close()

def find_similar_question(cursor, question_embedding):
    """Find the most similar question in the database."""
    question_embedding_str = "[" + ",".join(map(str, question_embedding.tolist())) + "]"
    cursor.execute(""" 
        SELECT qe.query_id, h.question, h.answer, qe.embedding
        FROM query_embeddings qe
        JOIN helpdesk h ON qe.query_id = h.query_id
        WHERE h.answer IS NOT NULL
        ORDER BY qe.embedding <-> VECTOR %s LIMIT 1;
    """, (question_embedding_str,))

    record = cursor.fetchone()

    if record:
        stored_embedding = np.array(ast.literal_eval(record[3]), dtype=np.float32)
        similarity = util.cos_sim(question_embedding, stored_embedding).item()
        if similarity >= 0.5:
            return record, similarity
    return None, None

@app.route('/api/helpdesk', methods=['POST'])
def post_question():
    new_question = request.json.get('newQuestion', '').strip()
    citizen_id = request.json.get('citizen_id', '')
    result = ask_question(citizen_id, new_question)
    return jsonify({'message': result})

@app.route('/api/helpdesk', methods=['GET'])
def get_faq():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM helpdesk WHERE answer IS NOT NULL")
    questions = cursor.fetchall()
    cursor.close()
    conn.close()

    faq_data = [{"question": q[0], "answer": q[1]} for q in questions]
    return jsonify(faq_data)

def ask_question(citizen_id, question):
    conn = connect_db()
    cursor = conn.cursor()

    question_embedding = get_embedding(question)
    similar_record, similarity = find_similar_question(cursor, question_embedding)

    if similar_record:
        print(f"Similar Question Found (Similarity: {similarity:.2f}):")
        print(f"Q: {similar_record[1]}\nA: {similar_record[2]}")
        return {"similar_question": similar_record[1], "answer": similar_record[2], "similarity": similarity}
    else:
        store_question_with_embedding(citizen_id, question)
        cursor.close()
        conn.close()
        return "Your question has been recorded and is awaiting an admin response."

if __name__ == "__main__":
    app.run(debug=True)
