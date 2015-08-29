#!/usr/bin/python3
#-*- coding: utf-8 -*-

import argparse
from hnmp import SNMP

    print ("RB SNR:", snr)
#snmp library source https://github.com/trehn/hnmp

class Radioparams:
    def __init__

# Argument parser
parser= argparse.ArgumentParser(
    prog = "get_radioconfig.py",
    description = "Obtain main config parameterso a wireless link device")
parser.add_argument('-d', '--device', required = True, 
    help = "IP address of the device")
parser.add_argument('-c', '--community', required = True,
    help = "SNMP community")
parser.add_argument('-v', '--version', default = 1,
    help = "SNMP protocol version")
args = parser.parse_args()

device = args.device
comm = args.community
ver = args.version

radio = SNMP(device, community=comm, version=ver)
try:
    device_info= radio.get("1.3.6.1.2.1.1.1.0")
except:
    print ("No SNMP response from ", device)

if device_info[:8] == "Alvarion":
    device_type = device_info[9:]
    print ("Vendor: Alvarion")
elif device_info == "Wireless Link":
    device_type = radio.get("1.3.6.1.4.1.4458.1000.1.1.30.0")
    print ("Vendor: Radwin")
elif device_info [:5] == "Linux":
    device_type = device_info [:6], "(UBNT Like)"
else:
    device_type = "unknown"
print ("Type  : ", device_type)

