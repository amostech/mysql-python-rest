# mysql-python-rest

This repo README has been tested with Debian Jessie 8. You can certainly use CentOS or other distros.

Debian AWS public image: debian-jessie-amd64-hvm-2016-11-13-1356-ebs - ami-0e79236b

## Database loading

**Database Information:**  
  
    Name: AirlineData  
    Description: On-time Flight Data for all flights in the United States from the Bureau of Transportation Statistics.  
    Time Range: Jan 01, 2018 - Feb 28, 2018  
    Number of records: 1058074  
    File: AirlineData.zip  

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


# Task #1 - SQL Query

    Answer the question: Return the count of flights that were delayed by more than 30 minutes per carrier.
    

# Task #2 - Rest API

    python api.py &> api.log &

## Run Jmeter 

    jmeter -n –t jmeter-api.jmx -l testresults.jtl
    
# Task #3 - Scaling strategies

  With the JMeter results you got and the logs of your API describe a strategy to improve the performance of this system.

