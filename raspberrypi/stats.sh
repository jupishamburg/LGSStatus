#!/bin/bash

URL="http://lgs-hh.geheimorganisation.org/append"
KEY="kai1photh1eiHeey1Quosh7ocaisaib4Efaidai4Ep"
TTY="/dev/ttyUSB0"
NET="192.168.178.0/24"

## network clients
curl ${URL}/clients?key=${KEY}\&value=`nmap -sn ${NET} | grep 'Host is up' | wc -l`

## temperature and door
echo "python2 ./temperature-door.py ${URL} ${KEY} ${TTY}"
