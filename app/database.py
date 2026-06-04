import psycopg2.pool

# Create a connection pool at module level
connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=20,
    host=DATABASE_HOST,
    database=DATABASE_NAME,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD
)

def get_db_connection():
    return connection_pool.getconn()

def release_db_connection(conn):
    connection_pool.putconn(conn)