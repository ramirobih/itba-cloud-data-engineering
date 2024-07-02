import pandas as pd
from sqlalchemy import create_engine

# connect db
engine = create_engine('postgresql://user:password@localhost:5432/flights')

queries = {
    "Aerolinea con mas retrasos": "SELECT airline, COUNT(*) AS total_delays FROM flights WHERE delay > 0 GROUP BY airline ORDER BY total_delays DESC LIMIT 1",
    "Dia con mas retrasos": "SELECT EXTRACT(DOW FROM departure_time) AS day_of_week, COUNT(*) AS total_delays FROM flights WHERE delay > 0 GROUP BY day_of_week ORDER BY total_delays DESC LIMIT 1",
    "Retrasos por mes": "SELECT EXTRACT(MONTH FROM departure_time) AS month, AVG(delay) AS avg_delay FROM flights WHERE delay > 0 GROUP BY month ORDER BY month",
    "Aeropuerto con mas retrasos": "SELECT origin_airport, COUNT(*) AS total_delays FROM flights WHERE delay > 0 GROUP BY origin_airport ORDER BY total_delays DESC LIMIT 1"
}

# run query
for query_name, query in queries.items():
    result = pd.read_sql_query(query, engine)
    print(f"Resultado para {query_name}:\n", result, "\n")