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
    "LocationID": "Int64",
    "Borough": "string",
    "Zone" : "string",
    "service_zone" : "string"
}

def run():
    """Ingestion pipeline that loads NYC taxi zone lookup data into PostgreSQL."""
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/'
    url = f'{prefix}/taxi_zone_lookup.csv'
    # Create a connection to the PostgreSQL database using SQLAlchemy
    engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')

        
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        iterator=True,
        chunksize=10)

    first = True
    for df_chunk in tqdm(df_iter):
        if first:
            df_chunk.head(n=0).to_sql(name='taxi_zone_lookup', 
                                      con=engine, 
                                      if_exists='replace'
                                      )
            first = False
        df_chunk.to_sql(name='taxi_zone_lookup', 
                        con=engine, 
                        if_exists='append'
                        )


# Entry point of the script
# Runs the ingestion pipeline when executed directly
if __name__ == '__main__':
    run()














