#!/bin/bash

URL="http://lgs-hh.geheimorganisation.org/append"
KEY="ieSohc0oochie6Reequungoo7quoza8NuRaing9una"
TTY="/dev/ttyUSB0"
NET="192.168.178.0/24"

## network clients

networkClientsAmount = `nmap -sn ${NET} | grep 'Host is up' | wc -l`
curl -d 'key=${KEY}\&value=${networkClientsAmount}' '${URL}/clients'

## temperature and door
python2 ./temperature-door.py ${URL} ${KEY} ${TTY}
