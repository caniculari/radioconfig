#!/usr/bin/python3
#-*- coding: utf-8 -*-

import argparse

# Argument parser
parser= argparse.ArgumentParser(
    prog = "get_radioconfig.py",
    description = "Obtain main config parameterso a wireless link device")
parser.add_argument('-d', '--device', required = True, help = "IP address of the device")
parser.add_argument('-c', '--community', required = True, help = "SNMP community")
args = parser.parse_args()

device = args.device
community = args.community

print ("Device: ", device)
print ("Community:", community)

