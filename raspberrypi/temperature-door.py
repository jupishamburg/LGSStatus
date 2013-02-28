#!/usr/bin/env python2
import sys
import serial
import requests

class Arduino(object):
	def __init__(self, serial):
		self.serial = serial
	def getLatestStatus(self):
		val=None
		while self.serial.inWaiting() > 0:
			status = self.serial.readline()
		return status

class Poster(object):
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

base_url = sys.argv[1]
security_token = sys.argv[2]
port = sys.argv[3]

s = serial.Serial(port=port)
arduino = Arduino(s)

status = arduino.getLatestStatus()
v = status.replace("\r\n", "").split(",")

door_state = "1" if (int(v[1]) > 150) else "0"
temperature = int(v[0]) - 12 # dirty hack because of electrical problems

poster = Poster()
poster.post_door_state(base_url, door_state, security_token)
poster.post_temperature(base_url, temperature, security_token)