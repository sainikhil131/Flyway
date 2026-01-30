import psycopg2

conn = psycopg2.connect(
    dbname="flyway_test",
    user="postgres",
    password="Mysql@123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='users'")
print(cur.fetchall())

cur.close()
conn.close()
