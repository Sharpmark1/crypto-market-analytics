import psycopg2

def connect_db():
    connection = psycopg2.connect(
        host="localhost",
        database="crypto_analytics",
        user="postgres",
        password="Mymailbox12569#",
        port="5432"
    )

    return connection