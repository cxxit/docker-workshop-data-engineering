#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

# ----------------------------
# Schema definition (ETL config)
# ----------------------------
# Controls how raw CSV data is parsed and transformed before loading into the database.
dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

def run(): 
    """
    Ingestion pipeline that loads NYC taxi trip data into PostgreSQL.

    This function performs an end-to-end ETL (Extract, Transform, Load) process:
    
    1. Extract:
       - Downloads NYC Yellow Taxi dataset from a remote compressed CSV source.
       - Reads data in chunks using pandas for memory efficiency.

    2. Transform:
       - Applies predefined data types to ensure schema consistency.
       - Parses datetime columns into proper datetime objects.

    3. Load:
       - Creates a PostgreSQL table (if not exists or replaces initial schema).
       - Inserts data into the target table in chunks using SQLAlchemy.

    Configuration:
        pg_user (str): PostgreSQL username
        pg_pass (str): PostgreSQL password
        pg_host (str): Database host (e.g., localhost)
        pg_port (int): Database port (default: 5432)
        pg_db (str): Database name
        year (int): Dataset year
        month (int): Dataset month
        chunksize (int): Number of rows per batch insert
        target_table (str): Destination table name in PostgreSQL

    Output:
        None
        Data is written directly into the PostgreSQL database.

    Notes:
        - Uses chunked ingestion to handle large datasets efficiently.
        - Requires a running PostgreSQL instance before execution.
        - Designed for reproducible ETL pipeline execution.
    """
    pg_user = 'root'
    pg_pass = 'root'
    pg_host = 'localhost'
    pg_port = 5432
    pg_db = 'ny_taxi'

    year = 2021
    month = 1
    chunksize = 100000
    target_table = 'yellow_taxi_date'

    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    url = f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'
    engine = create_engine(f'postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    # extract 
    df_iter = pd.read_csv(
    url,
    dtype=dtype, # trasnform data type 
    parse_dates=parse_dates, # trasnform datetime
    iterator=True,
    chunksize=chunksize
    )

    first = True
    for df_chunk in tqdm(df_iter):
        if first: 
            df_chunk.head(n=0).to_sql(
                name=target_table,
                con=engine, 
                if_exists='replace'
                )
            first = False
        # ingestion script (load)
        df_chunk.to_sql(
            name=target_table, 
            con=engine, 
            if_exists='append')
        

# Entry point of the script
# Runs the ingestion pipeline when executed directly
if __name__ == '__main__':
    run()



