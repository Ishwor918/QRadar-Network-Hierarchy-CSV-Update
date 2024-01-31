In QRadar, Network hierarchy can be implemented by defining all the network subnet in csv and using the script. The format of CSV is attached within this repo named "Network Hierarchy Format.csv"

To run the python script, you must provide two paths i.e., one is for locating csv file and other is for generating json file.

After generating json file, we need to push the output via api. Go to QRadar Console, navigate to Interactive API developer --> Config --> Network Hierarchy --> Staged Network and then go to PUT option. Within the query section, copy all the output of JSON file and paste it and click on "Try it out" and Boom!!!!. Navigate to Admin and perform deploy change to make the change live.
