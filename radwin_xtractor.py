#!/usr/bin/python3
#-*- encoding: utf-8 -*-

import sys
import binascii
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

hardware_info = { '1) Name': "1.3.6.1.2.1.1.5.0",
    '2) Contact': ".1.3.6.1.2.1.1.4.0",
    '3) Location' : ".1.3.6.1.2.1.1.6.0",
    '4) MAC-Address' : ".1.3.6.1.2.1.2.2.1.6.1",
    '5) Product' : ".1.3.6.1.4.1.4458.1000.1.1.30.0",
    '6) Serial number' : ".1.3.6.1.4.1.4458.1000.1.1.29.0",
    '7) Hardware version' : ".1.3.6.1.4.1.4458.1000.1.1.2.0",
    '8) Software version' : ".1.3.6.1.4.1.4458.1000.1.1.3.0",
    }

link_info = { '1) Link ID' : '.1.3.6.1.4.1.4458.1000.1.5.3.0',
    '2) Installation Frequency' : '.1.3.6.1.4.1.4458.1000.1.5.1.0',
    '3) Current Frequency' : '1.3.6.1.4.1.4458.1000.1.5.16.0',
    '4) Channel BW' : '.1.3.6.1.4.1.4458.1000.1.5.51.0',
    '5) Band' : '.1.3.6.1.4.1.4458.1000.1.5.53.4.0',
    '6) Antenna Type' : '.1.3.6.1.4.1.4458.1000.1.5.64.0',
    '10) Tx Power': '.1.3.6.1.4.1.4458.1000.1.5.50.0',
    '8) Antenna gain': '1.3.6.1.4.1.4458.1000.1.5.42.0',
    '7) Antenna Mode': '.1.3.6.1.4.1.4458.1000.1.5.58.0',
    '9) Tranmission Type': '1.3.6.1.4.1.4458.1000.1.5.58.0',
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
#hardware_info['4) MAC-Address'] = binascii.b2a_hex(hardware_info['4) MAC-Address']).decode("utf-8")
link_info['10) Tx Power'] = str(link_info['10) Tx Power']) + " dBm"
link_info["8) Antenna gain"] = str(link_info["8) Antenna gain"])[0:2] + "." + str(link_info["8) Antenna gain"])[2:] 
link_info["4) Channel BW"] = link_info["4) Channel BW"][5:7]
if link_info['9) Tranmission Type'] == 1:
    link_info['9) Tranmission Type'] = "MIMO"
elif link_info['9) Tranmission Type'] == 2:
    link_info['9) Tranmission Type'] = "Diversity"
if link_info['1) Link ID'][0:8] == "SELUCREH":
    link_info['1) Link ID'] = link_info['1) Link ID'][8:]
if link_info['7) Antenna Mode'] == 1:
    link_info['7) Antenna Mode'] = "Single"
elif  link_info['7) Antenna Mode'] == 2:
    link_info['7) Antenna Mode'] = "Dual"
if link_info["6) Antenna Type"] == 1:
    link_info["6) Antenna Type"] = "External"
elif link_info["6) Antenna Type"] == 2:
    link_info["6) Antenna Type"] = "Integrated"
elif link_info["6) Antenna Type"] == 3:
    link_info["6) Antenna Type"] = "Embedded external"
elif link_info["6) Antenna Type"] == 4:
    link_info["6) Antenna Type"] = "Embedded integrated"

# Sort
hi = sorted(hardware_info.items(), key=lambda t: t[0])

print ("----- Hardware info -----")
for i, j in sorted(hardware_info.items(), key=lambda t: t[0]):
    print (i, ':', j)
print ("----- Link info -----")
for i, j in sorted(link_info.items(), key=lambda t: t[0]):
    print (i, ':', j)
print ("----- Network info -----")
for i, j in network_info.items():
    print (i, ':', j)


