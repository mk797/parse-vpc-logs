import csv
from collections import defaultdict

# Load the lookup table
def read_lookup_table(file_path):
    #dictionary to store lookup table data
    tag_mapping = {}  
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # print(row)
            port_protocol = (int(row['dstport']), row['protocol'].strip().lower())
            tag_mapping[port_protocol] = row['tag'].strip()
    return tag_mapping


# Parse the rows in VPC flow logs and map them to respective tags
def process_flow_logs(log_file_path, tag_mapping):
    #dictionary to track the respective tag counts
    tag_counters = defaultdict(int)
    #dictionary to track the respective protocol counts  
    port_protocol_counters = defaultdict(int)  
    
    with open(log_file_path, mode='r') as file:
        for line in file:
            columns = line.split()
            # print(len(columns))
            destination_port = int(columns[5]) #extract dst port
            protocol_number = int(columns[7])  #extract protocol number
            
            # Map protocol number to its corresponding protocol name
            protocol_name = protocol_number_to_name(protocol_number)
            port_protocol = (destination_port, protocol_name)
            
            if port_protocol in tag_mapping:
                #extract corresponding tag
                assigned_tag = tag_mapping[port_protocol]
            else:
                assigned_tag = "Untagged"
            
            tag_counters[assigned_tag] += 1  # increment tag count
            port_protocol_counters[port_protocol] += 1  #increment port-protocol counts
    
    return tag_counters, port_protocol_counters


# Protocol number to protocol name mapper function.
def protocol_number_to_name(protocol_number):
    protocol_map = {
        1: 'icmp',
        6: 'tcp',
        17: 'udp',
    }
    return protocol_map.get(protocol_number, 'unknown')


# output the results to a text file
def output_results_to_file(tag_counters, port_protocol_counters, output_file_path):
    with open(output_file_path, mode='w') as file:
        file.write("Tag Counts:\n")
        file.write("Tag,Count\n")
        for tag, count in sorted(tag_counters.items()):
            file.write(f"{tag},{count}\n")
        
        file.write("\nPort/Protocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in sorted(port_protocol_counters.items()):
            file.write(f"{port},{protocol},{count}\n")


def main():
    lookup_table_path = 'lookup_table.csv'
    flow_log_path = 'vpc_flow_logs.txt'
    result_output_path = 'output_results.txt'
    
    #read lookup table and load the data to dictionary
    tag_mapping = read_lookup_table(lookup_table_path)
    #corresponding tag and port_protocol combination counters
    tag_counters, port_protocol_counters = process_flow_logs(flow_log_path, tag_mapping)
    output_results_to_file(tag_counters, port_protocol_counters, result_output_path)

if __name__ == '__main__':
    main()
