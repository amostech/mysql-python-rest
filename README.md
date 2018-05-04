# mysql-python-rest

## Database loading

Write here the instructions for which file to load into the database and the URL of the MySQL instance

### Create Table

```
CREATE TABLE airlinedatadb.flights (
  FL_DATE date NULL,
  UNIQUE_CARRIER varchar(45) NULL,
  AIRLINE_ID varchar(45) NULL,
  CARRIER varchar(45) NULL,
  ORIGIN_AIRPORT_ID int NULL,
  ORIGIN_AIRPORT_SEQ_ID int NULL,
  ORIGIN_CITY_MARKET_ID int NULL,
  DEST_AIRPORT_ID int NULL,
  DEST_AIRPORT_SEQ_ID int NULL,
  DEST_CITY_MARKET_ID int NULL,
  CRS_DEP_TIME int NULL,
  DEP_TIME int NULL,
  DEP_DELAY int NULL,
  CRS_ARR_TIME int NULL,
  ARR_TIME int NULL,
  ARR_DELAY int NULL,
  CANCELLED int NULL,
  DIVERTED int NULL,
  CARRIER_DELAY int NULL,
  WEATHER_DELAY int NULL,
  NAS_DELAY int NULL,
  SECURITY_DELAY int NULL,
  LATE_AIRCRAFT_DELAY int NULL
);
```

# Loading the data

    - Copy file into /var/lib/mysql-files
    - Make sure to run your mysql session with --local-infile option

    LOAD DATA LOCAL INFILE "AirlineData.csv" INTO TABLE flights FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;


# Task Number 1

    Answer the question: Return the count of flights that were delayed by more than 30 minutes per carrier.
    

## REST API

    python api.py &> api.log &

## Run Jmeter 

    jmeter -n –t jmeter-api.jmx -l testresults.jtl

