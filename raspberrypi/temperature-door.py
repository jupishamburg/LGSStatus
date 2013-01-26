#!/usr/bin/env python2

import sys
import time

import serial
import requests

def post_door_state(base_url, door_state, security_token):
	params = {
		'value': door_state,
		'key': security_token
	}
	requests.post(base_url + "/door", params)

def post_temperature(base_url, temperature, security_token):
	params = {
		'value': temperature,
		'key': security_token
	}
	requests.post(base_url + "/temperature", params)

# TODO: This should be mockable
if True:
	base_url = sys.argv[1]
	security_token = sys.argv[2]
	port = sys.argv[3]

	s = serial.Serial(port=port)
	s.flushInput()
	s.flushOutput()

	# get the key-pair from the arduino
	if s.write("k") is 1:
		v = s.readline().replace("\r\n", "").split(",")

	door_state = "1" if (int(v[1]) > 150) else "0"
	temperature = int(v[0]) - 12 # dirty hack because of electrical problems
else:
	#Temporary Mock
	print "Should not be run on live server :D"
	base_url = "http://0.0.0.0:8080/append"
	door_state = "1"
	temperature = "52"
	security_token = "YOUR_PERSONAL_WEBSERVER_ACCESS_TOKEN"

post_door_state(base_url, door_state, security_token)
post_temperature(base_url, temperature, security_token)

