#!/usr/bin/python3
#-*- encoding: utf-8 -*-

import sys
from hnmp import SNMP

# variable inicialization
hostname = sys.argv[1]
comm = "netman"
radio = SNMP (hostname, community=comm, version=1)

print ("Getting info...")

# Error handling during query to device
try:
    name = radio.get(".1.3.6.1.2.1.1.5.0")
except:
    print ("Error: No SNMP response received before timeout")
    sys.exit(1)

# diccionary of values defined for snmp query

hardware_info = { 'Name': "1.3.6.1.2.1.1.5.0",
    'Contact': ".1.3.6.1.2.1.1.4.0",
    'Location' : ".1.3.6.1.2.1.1.6.0",
    'MAC-Address' : ".1.3.6.1.2.1.2.2.1.6.1",
    'Product' : ".1.3.6.1.4.1.4458.1000.1.1.30.0",
    'Serial number' : ".1.3.6.1.4.1.4458.1000.1.1.29.0",
    'Hardware version' : ".1.3.6.1.4.1.4458.1000.1.1.2.0",
    'Software version' : ".1.3.6.1.4.1.4458.1000.1.1.3.0",
    }

link_info = { 'link id' : '.1.3.6.1.4.1.4458.1000.1.5.3.0',
    'Installation Frequency' : '.1.3.6.1.4.1.4458.1000.1.5.1.0',
    'Current Frequency' : '1.3.6.1.4.1.4458.1000.1.5.16.0',
    'Channel BW' : '.1.3.6.1.4.1.4458.1000.1.5.51.0',
    'Band' : '.1.3.6.1.4.1.4458.1000.1.5.53.4.0',
    'Antenna type' : '.1.3.6.1.4.1.4458.1000.1.5.48.0',
    'Tx Power': '.1.3.6.1.4.1.4458.1000.1.5.50.0',
}
network_info = { 'IP address' : '.1.3.6.1.4.1.4458.1000.1.1.6.0',
    'Netmask' : '.1.3.6.1.4.1.4458.1000.1.1.7.0',
    'Default gateway' : '.1.3.6.1.4.1.4458.1000.1.1.8.0',
}

#query device for values and store in dictionary

for i, j in hardware_info.items():
    #print( i, ':', radio.get(j))
    hardware_info[i] = radio.get(j)
for i, j in link_info.items():
    #print( i, ':', radio.get(j)
    link_info[i] = radio.get(j) 
for i, j in network_info.items():
    #rint( i, ':', radio.get(j))
    network_info[i] = radio.get(j)

# Change representation of some definitions
#hardware_info['MAC-Address'] = hardware_info['MAC-Address']

print (hardware_info)
