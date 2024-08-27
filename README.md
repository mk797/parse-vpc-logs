# VPC Flow Log Tagging Program

## Overview

This program analyzes VPC flow logs and assigns tags to each entry based on a predefined lookup table that maps `dstport` and `protocol` values to a specific tag. The program generates an output file summarizing the number of entries associated with each tag and each port-protocol combination.

## Files

- **`parse_vpc_logs.py`**: The main program that processes the flow log entries and assigns tags.
- **`lookup_table.csv`**: A CSV file containing mappings in the format `dstport,protocol,tag`.
- **`vpc_flow_logs.txt`**: A text file containing the VPC flow logs to be analyzed.
- **`output_results.txt`**: The output file generated by the program, containing the count of each tag and port-protocol combination.


## Assumptions and Considerations
Log Format:

The program only supports the default log format as per AWS VPC Flow Logs documentation.
Only version 2 of the VPC flow log format is supported.
The log file must contain all the required fields as specified in the default format.
Case Insensitivity:

The protocol values in the lookup table and flow logs are handled in a case-insensitive manner. The program converts all protocol values to lowercase before performing any comparisons.
Unmatched Entries:

Entries that do not match any combination of dstport and protocol in the lookup table are tagged as "Untagged".
Protocol Mapping:

The program includes a basic protocol mapping for common protocols like TCP, UDP, and ICMP. Any protocols not listed in the predefined mapping are labeled as "unknown".
Output Format:

The output file (output_results.txt) includes two sections:
Tag Counts: A summary of the number of entries associated with each tag.
Port/Protocol Combination Counts: A summary of the number of entries for each unique dstport/protocol combination.
## Prerequisites

- Python 3.x

## Steps to Run the Program

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mk797/parse-vpc-logs.git
2. **Navigate to the project directory**:
   ```bash
   cd parse-vpc-logs
3. **Run the Python program**:
   ```bash
   python3 parse_vpc_logs.py

**View the output**:

After running the program, the results will be saved in the output_results.txt file in the same directory.
