CREATE DATABASE metrobus;

-- Switch connection to a new database
\c metrobus;

-- create table vehicle
CREATE TABLE vehicle(
    id bigserial NOT NULL,
    label integer,
    current_status integer,
    PRIMARY KEY (id)
);

-- create table city
CREATE TABLE city(
    id bigserial NOT NULL,
    name varchar(50),
    PRIMARY KEY (id)
);

-- create table ubication
CREATE TABLE ubication(
    id bigserial NOT NULL,
    latitude float,
    longitude float,
    vehicle_id bigint NOT NULL,
    city_id bigint NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(id),
    FOREIGN KEY (city_id) REFERENCES city(id)
);




-- inserts of examples
-- INSERT INTO vehicle (id, label, current_status) VALUES (1,235,2);
-- INSERT INTO city (id, name) VALUES (1,'Coyoacán');
-- INSERT INTO ubication (id,latitude, longitude, vehicle_id, city_id) VALUES (1,19.3147846,-99.1876256,1,1);


-- INSERT INTO vehicle (id, label, current_status) VALUES (2,245,1);
-- INSERT INTO city (id, name) VALUES (2,'Gustavo A. Madero');
-- INSERT INTO ubication (id,latitude, longitude, vehicle_id, city_id) VALUES (2,19.5647846,-99.1975256,2,2);