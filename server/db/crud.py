import psycopg2

from config import (
    DB_HOST,
    DB_PORT,
    POSTGRES_DB,
    POSTGRES_PASSWORD,
    POSTGRES_USER,
)


def investment_journal(data):
    create_table_query = """
        CREATE TABLE IF NOT EXISTS investments (
            id SERIAL PRIMARY KEY,
            user_full_name VARCHAR(255) NOT NULL,
            initialDeposit NUMERIC NOT NULL,
            interestRate NUMERIC NOT NULL,
            investmentPeriod INTEGER NOT NULL,
            compoundFrequency VARCHAR(255) NOT NULL,
            total NUMERIC NOT NULL
        )
    """
    insert_query = """
        INSERT INTO investments (user_full_name,
            initialDeposit,
            interestRate,
            investmentPeriod,
            compoundFrequency,
            total)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    with psycopg2.connect(
        host=DB_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=DB_PORT
    ) as connect:
        with connect.cursor() as cursor:
            cursor.execute(create_table_query)
            cursor.execute(
                insert_query, (
                    data['investorFullName'],
                    int(data['initialDeposit']),
                    data['interestRate'],
                    data['investmentPeriod'],
                    str(data['compoundFrequency']),
                    data['total']
                )
            )
    connect.commit()
