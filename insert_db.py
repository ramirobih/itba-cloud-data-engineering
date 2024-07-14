import pandas as pd
from sqlalchemy import create_engine

# load file
df = pd.read_csv('/app/Airlines.csv')
# connect db
engine = create_engine('postgresql://user:password@postgres_itba:5432/flights')
# insert
df.to_sql('flights', con=engine, if_exists='append', index=False)