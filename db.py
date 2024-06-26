import os
import pandas as pd
from sqlalchemy import create_engine

# Retrieve database connection details from environment variables
db_type = 'postgresql'
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

# Create the SQLAlchemy engine
engine = create_engine(f'{db_type}://{username}:{password}@{host}:{port}/{database}')

# Load your cleaned datasets
df1 = pd.read_csv('qb.csv')
df2 = pd.read_csv('rb.csv')
df3 = pd.read_csv('wrte.csv')

# Upload the DataFrame to AWS RDS
df1.to_sql('qb', con=engine, if_exists='replace', index=False)
df2.to_sql('rb', con=engine, if_exists='replace', index=False)
df3.to_sql('wrte', con=engine, if_exists='replace', index=False)

print("DataFrames successfully uploaded to AWS RDS")
