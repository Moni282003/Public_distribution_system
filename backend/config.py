import os

class Config:
    # Database credentials
    USER = os.getenv('DB_USER', 'postgres')
    PASSWORD = os.getenv('DB_PASSWORD', '123456')
    HOST = os.getenv('DB_HOST', 'localhost')
    PORT = os.getenv('DB_PORT', '5432')  # Default PostgreSQL port
    DATABASE = os.getenv('DB_DATABASE', 'login')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
