#!/bin/bash
NET="192.168.178.0/24"
nmap -sn ${NET} | grep 'Host is up' | wc -l
