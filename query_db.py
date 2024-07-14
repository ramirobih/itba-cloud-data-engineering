import pandas as pd
import psycopg2 

# connect db
con = psycopg2.connect(
    host="postgres_itba",
    database="flights",
    user="user",
    password="password"
)

cursor = con.cursor()

queries = {
    'Aerolinea con mas retrasos': 'SELECT flights."Airline", COUNT(*) AS total_delays FROM flights WHERE "Delay" > 0 GROUP BY flights."Airline" ORDER BY total_delays DESC LIMIT 1',
    'Dia con mas retrasos': 'SELECT "DayOfWeek" AS day_of_week, COUNT(*) AS total_delays FROM flights WHERE "Delay" > 0 GROUP BY day_of_week ORDER BY total_delays DESC LIMIT 1',
    #'Retrasos por mes': 'SELECT EXTRACT(MONTH FROM departure_time) AS month, AVG(delay) AS avg_delay FROM flights WHERE delay > 0 GROUP BY month ORDER BY month',
    'Aeropuerto con mas retrasos': 'SELECT "AirportFrom" , COUNT(*) AS total_delays FROM flights WHERE "Delay" > 0 GROUP BY "AirportFrom" ORDER BY total_delays DESC LIMIT 1'
}

# run query
for query_name, query in queries.items():
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    #print(f"Resultado para {query_name}:\n", result, "\n")