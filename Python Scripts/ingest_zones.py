#!/usr/bin/env python
# coding: utf-8

import os
import sys
import argparse
# from signal import pause

import pandas as pd
from sqlalchemy import create_engine

def main(params):
  user = params.user
  password = params.password
  host = params.host
  port = params.port
  db = params.db
  table_name = params.table_name
  csv_name = 'zones.csv'

  engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

  df = pd.read_csv(csv_name)
  df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
  df.to_sql(name=table_name, con=engine, if_exists='append')
  print('Finished inserting zones to database')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
  parser.add_argument('--user', help='Username for posrgres')
  parser.add_argument('--password', help='Password for postgres')
  parser.add_argument('--host', help='Hostmane for postgres')
  parser.add_argument('--port', help='Port for postgres')
  parser.add_argument('--db', help='Database name')
  parser.add_argument('--table_name', help='Table name')
  
  args = parser.parse_args()
  
  main(args)