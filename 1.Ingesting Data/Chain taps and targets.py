# In the shell, pipe the output of your Singer “tap”, tap-marketing-api, to target-csv.
# Pass the configuration file data_lake.conf (located in the ingest folder of the data lake) to target-csv, 
# using the --config flag. The configuration file specifies where the CSV file should be written to and should not be changed.
# Execute your command and click on “Submit Answer”, below, to see if you got it right.
repl:~/workspace$ tap-marketing-api | target-csv --config ingest/data_lake.conf
