CREATE TABLE train
(
    train_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    code VARCHAR(255)
);

CREATE TABLE journey
(
    journey_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    departure_time DATETIME,
    arrival_time DATETIME,
    departure_platform VARCHAR(255),
    arrival_platform VARCHAR(255),
    type_journey VARCHAR(255),
    train_id INT,
    FOREIGN KEY (train_id) REFERENCES train(train_id)
);

CREATE TABLE transfer_station
(
    transfer_station_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    order_in_journey INT,
    journey_id INT,
    station_id INT,
    FOREIGN KEY (journey_id) REFERENCES journey(journey_id),
    FOREIGN KEY (station_id) REFERENCES station(station_id)
);

CREATE TABLE station
(
    station_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    station_name VARCHAR(255),
    platform_number VARCHAR(255),
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES city(city_id)
);

CREATE TABLE city
(
    city_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    city_name VARCHAR(255),
    postal_code VARCHAR(255)
);
