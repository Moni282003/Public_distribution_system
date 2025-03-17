import psycopg2
from datetime import datetime
import logging

DB_HOST = 'localhost'  
DB_USER = 'postgres'   
DB_PASS = '123456'     
DB_NAME = 'kms'   

logging.basicConfig(level=logging.DEBUG)

def get_db_connection(DB_NAME):
    """Establish a database connection."""
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

def answer_question():
    """Function to handle admin answering questions."""
    try:
        conn = get_db_connection(DB_NAME)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT query_id, question, asked_by FROM helpdesk WHERE answer IS NULL"
        )
        questions = cursor.fetchall()

        if not questions:
            print("No unanswered questions.")
        else:
            print("Unanswered Questions:")
            for q in questions:
                print(f"Query ID: {q[0]}, Question: {q[1]}, Asked By Citizen ID: {q[2]}")

            query_id = int(input("Enter the Query ID you want to answer: "))
            answer = input("Enter your answer: ")
            admin_id = int(input("Enter your Admin ID: "))  # Admin ID as integer

            cursor.execute(
                """
                UPDATE helpdesk
                SET answer = %s, answered_by = %s, answered_at = %s
                WHERE query_id = %s;
                """,
                (answer, admin_id, datetime.now(), query_id),
            )
            conn.commit()

            print(f"Answer recorded for Query ID {query_id}.")

    except Exception as e:
        logging.error(f"Error while processing the question: {e}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    print("Welcome, Admin!")
    answer_question()
