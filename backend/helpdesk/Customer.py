import psycopg2
import numpy as np
import logging
from sentence_transformers import SentenceTransformer, util

DB_HOST = 'localhost'  
DB_USER = 'postgres'   
DB_PASS = '123456'     
DB_NAME = 'kms'  

logging.basicConfig(level=logging.DEBUG)

MODEL = SentenceTransformer("all-MiniLM-L6-v2")

def get_db_connection():
    """Establish a database connection."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to the database: {e}")
        return None

def find_similar_question(cursor, question_embedding):
    """Find the most similar question in the database."""
    cursor.execute("""
        SELECT qe.query_id, qe.embedding, h.question, h.answer
        FROM query_embeddings qe
        JOIN helpdesk h ON qe.query_id = h.query_id
        WHERE h.answer IS NOT NULL
    """)
    records = cursor.fetchall()

    if not records:
        return None, None

    similarities = []
    for record in records:
        stored_embedding = np.frombuffer(record[1], dtype=np.float32)
        similarity = util.cos_sim(question_embedding, stored_embedding).item()
        similarities.append((record, similarity))

    most_similar = max(similarities, key=lambda x: x[1])
    most_similar_record, highest_similarity = most_similar

    if highest_similarity >= 0.8:  # Adjust threshold as needed
        return most_similar_record, highest_similarity

    return None, None

def ask_question():
    """Function to handle customer question submission."""
    conn = get_db_connection()
    if not conn:
        logging.error("Database connection failed.")
        return

    cursor = conn.cursor()

    citizen_id = input("Enter your Citizen ID: ")
    question = input("Enter your question: ")

    question_embedding = MODEL.encode(question)

    similar_record, similarity = find_similar_question(cursor, question_embedding)
    if similar_record:
        print(f"Similar Question Found (Similarity: {similarity:.2f}):")
        print(f"Q: {similar_record[2]}\nA: {similar_record[3]}")
    else:
        cursor.execute(
            "INSERT INTO helpdesk (question, asked_by) VALUES (%s, %s) RETURNING query_id",
            (question, citizen_id),
        )
        query_id = cursor.fetchone()[0]

        cursor.execute(
            "INSERT INTO query_embeddings (query_id, embedding) VALUES (%s, %s)",
            (query_id, question_embedding.tobytes()),
        )
        conn.commit()
        print(f"Your question has been recorded. Query ID: {query_id}. Please wait for an admin to respond.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    print("Welcome, Customer!")
    ask_question()
