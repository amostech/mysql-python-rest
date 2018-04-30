# mysql-python-rest

## Database loading

Write here the instructions for which file to load into the database and the URL of the MySQL instance

### Create Table

CREATE TABLE `airlinedatadb`.`flights` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `FL_DATE` DATE NULL,
  `UNIQUE_CARRIER` VARCHAR(45) NULL,
  `AIRLINE_ID` VARCHAR(45) NULL,
  `CARRIER` VARCHAR(45) NULL,
  `ORIGIN_AIRPORT_ID` INT NULL,
  `ORIGIN_AIRPORT_SEQ_ID` INT NULL,
  `ORIGIN_CITY_MARKET_ID` INT NULL,
  `DEST_AIRPORT_ID` INT NULL,
  `DEST_AIRPORT_SEQ_ID` INT NULL,
  `DEST_CITY_MARKET_ID` INT NULL,
  `CRS_DEP_TIME` INT NULL,
  `DEP_TIME` INT NULL,
  `DEP_DELAY` INT NULL,
  `CRS_ARR_TIME` INT NULL,
  `ARR_TIME` INT NULL,
  `ARR_DELAY` INT NULL,
  `CANCELLED` INT NULL,
  `DIVERTED` INT NULL,
  `CARRIER_DELAY` INT NULL,
  `WEATHER_DELAY` INT NULL,
  `NAS_DELAY` INT NULL,
  `SECURITY_DELAY` INT NULL,
  `LATE_AIRCRAFT_DELAY` INT NULL,
  PRIMARY KEY (`id`));

# Loading the data

    - Copy file into /var/lib/mysql-files
    - Make sure to run your mysql session with --local-infile option

    LOAD DATA LOCAL INFILE "AirlineData.csv" INTO TABLE flights FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;


# Task Number 1

    Answer the question: Return the count of flights that were delayed by more than 30 minutes per carrier.
    

## REST API

    