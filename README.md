# Car Rental Report: User Guide. 

````
1. From your repo folder, clone the code and checkout to your branch
    a. git clone https://github.com/effisamm/gr-coding-challenge.git
    b. cd car_rentals_etl_job
    c. git checkout <branch name>
````

````
2. Install, relevent libraries and run the pipeline
    a. Install IDE prefably PyCharm
    b. Please note this application uses the python 2.7 version
    c. pip install ijson
    d. Click on start to run the pipeline or "Shift + f10"
````

# Assumptions

````
1. Utilization of ijson over json and Apache Spark
    a. With the assumption of processing large input json file, utilizing json wouln't be 
    ideal because they would be too large to fit into memory. In this usecase ijson is utilized
    to parse JSON objects incremetally and extract elements without loading the entire file thus 
    making it memory efficient
    
    b. Data sources often come from different sources, with ijson we can ingest data from HTTP streams
    and process at a much faster rate 
    
    c. Apache spark or pyspark were not used in this project due to lack of limited resources and 
    distributed file systems.

````

````
2. Json data

    a. Start:
        i) Assumed the type and IDs were in the correct format and commas were present
        ii) Utilized the session ID and start time from the dictionary object with the assumption
        of valid data.  
    b. End:
        i) Assumed the timestamps would have inaccurate data so created a try and except block to catch
        the errors, fix the issue with appropriate time and re-run the pipeline with updated
        json file. 
````

# New possible Features to enhance pipeline

````
1. Integrate bash script into the pipeline to run on linux terminal (3sp)
2. Save Json and csv file with dates to keep track of file processed,
   example(rental_reports_20221009.json) (2sp)
3. If same file is processed overwrite files (1sp)
4. Create Airflow DAGs to trigger automated pipeline end to end (5sp)
5. For Distributed database and sources, change "rental_processing.py" codebase
   to utilize pyspark (3sp)
6. Load rental report summary files in parquet format for compression efficiency (1sp)
7. Update Readme with new configurations and intructions on running the pipeline (1sp)

````