import pandas as pd
from sqlalchemy import create_engine

# load file
df = pd.read_csv('path/to/Airlines.csv')
# connect db
engine = create_engine('postgresql://user:password@localhost:5432/flights')
# insert
df.to_sql('flights', engine, if_exists='append', index=False)