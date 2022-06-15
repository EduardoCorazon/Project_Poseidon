# By: Eduardo Corazon
#Date: 5/31/2022
#Description: This is a
#

#!/usr/bin/python

# imports
import scapy.all as scapy
import re

############################### Stage 1 #################

# ARP Scan
# used to make sure we input a valid IP range
validateIP = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
    ipRange = input(
        "\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
    if validateIP.search(ipRange):
        print(f"{ipRange} is a valid ip address range")
        break

arp_result = []
arp_result.append(scapy.arping(ipRange))  # print out arp scan

for i in arp_result:
    print("testworked")


# Select the IP


############################### Stage 2 #################


############################### Stage 3 #################
