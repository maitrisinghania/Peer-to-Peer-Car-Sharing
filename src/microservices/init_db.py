
"""
Database initialization script for ShareARider

This script creates the necessary PostgreSQL databases for all microservices.
It requires psycopg2 and the PostgreSQL server to be running.

Usage:
    python init_db.py
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Configuration
postgres_host = "localhost"
postgres_user = "postgres"
postgres_password = "postgres"
databases = ["sharearider_users", "sharearider_cars", "sharearider_bookings"]

def create_database(db_name):
    # Connect to PostgreSQL server
    conn = psycopg2.connect(
        host=postgres_host,
        user=postgres_user,
        password=postgres_password
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    
    try:
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' created successfully.")
    except psycopg2.errors.DuplicateDatabase:
        print(f"Database '{db_name}' already exists.")
    finally:
        cursor.close()
        conn.close()

def main():
    print("Initializing ShareARider databases...")
    for db in databases:
        create_database(db)
    print("Database initialization completed.")

if __name__ == "__main__":
    main()
