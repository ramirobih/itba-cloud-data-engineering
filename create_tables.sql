CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    airline VARCHAR(50),
    flight_number VARCHAR(10),
    origin_airport VARCHAR(50),
    destination_airport VARCHAR(50),
    departure_time TIMESTAMP,
    arrival_time TIMESTAMP,
    delay INTEGER
);