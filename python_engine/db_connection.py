import os
from sqlalchemy import create_engine
import pandas as pd


def get_engine(user="postgrese", password="postgrese", host="localhost", port=5432, dbname="netflix_table"):

    user = user
    password = password
    host = host
    port = port
    dbname = dbname

    if not all([user, password, dbname]):
        raise ValueError("Database credentials (user, password, dbname) are required")

    url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    return create_engine(url)


if __name__ == "__main__":
    engine = get_engine()
    print("Engine created:", engine)

    df = pd.read_sql("SELECT * FROM netflix_titles", engine)