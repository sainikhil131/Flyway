import psycopg2

def get_conn():
    return psycopg2.connect(
        host="localhost",
        dbname="flyway_test",
        user="postgres",
        password="Mysql@123",
        port=5432
    )
