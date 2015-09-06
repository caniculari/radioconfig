#!/usr/bin/python3
#-*- encoding: utf-8 -*-

from hnmp import SNMP

hostname = "10.0.10.220"
comm = "netman"

hardware_info = { 'name': ".1.3.6.1.2.1.1.5.0",
    'contact': ".1.3.6.1.2.1.1.4.0",
    'location' : ".1.3.6.1.2.1.1.6.0",
    'mac-address' : ".1.3.6.1.2.1.2.2.1.6.1",
    'product' : ".1.3.6.1.4.1.4458.1000.1.1.30.0",
    'serial number' : ".1.3.6.1.4.1.4458.1000.1.1.29.0",
    'hardware version' : ".1.3.6.1.4.1.4458.1000.1.1.2.0",
    'software version' : ".1.3.6.1.4.1.4458.1000.1.1.3.0",
    }

link_info = { 'link id' : '.1.3.6.1.4.1.4458.1000.1.5.3.0',
    'Installation Frequency' : '.1.3.6.1.4.1.4458.1000.1.5.1.0',
    'Current Frequency' : '1.3.6.1.4.1.4458.1000.1.5.16.0',
    'Channel BW' : '.1.3.6.1.4.1.4458.1000.1.5.51.0',
    'Band' : '.1.3.6.1.4.1.4458.1000.1.5.53.4.0',
    'Antenna type' : '.1.3.6.1.4.1.4458.1000.1.5.48.0',
    'Tx Power': '.1.3.6.1.4.1.4458.1000.1.5.50.0',
}
network_info = { 'ip address' : '.1.3.6.1.4.1.4458.1000.1.1.6.0',
    'mask' : '.1.3.6.1.4.1.4458.1000.1.1.7.0',
    'gateway' : '.1.3.6.1.4.1.4458.1000.1.1.8.0',
}

radio = SNMP (hostname, community=comm, version=1)
print ('-----Hardware Information-----')
for i, j in hardware_info.items():
    print( i, ':', radio.get(j))
print ('-----Link Information-----')
for i, j in link_info.items():
    print( i, ':', radio.get(j))
print ('-----Network Information-----')
for i, j in network_info.items():
    print( i, ':', radio.get(j))
