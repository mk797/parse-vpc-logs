**VPC Fow Log Tagging program**

**Overview**

This program analyzes VPC flow logs and assigns tags to each entry based on a predefined lookup table 
that maps 'dstport' and 'protocol' values to a specific tag.
It outputs a result that shows the number of entries associated with each tag and each port-protocol combination to a text file.


**Files:**
1. parse_vpc_logs.py - program which assigns the logs entries to tags.
2. lookup_table.csv  - a CSV file that contains dstport, protocol, and corresponding tag in the format dstport,protocol,tag
3. vpc_flow_logs.txt    - text file that contains VPC logs.
3. output_results.txt   - output text file from the program that contains a number of tags and the number of port-protocol combinations.

**Steps to run the program**

Run the below commands
1. clone this git repo
>  git clone https://github.com/mk797/parse-vpc-logs.git
2. set the current directory as the project directory
>   cd parse-vpc-logs
3. run the python progam
>   python3 parse_vpc_logs.py
