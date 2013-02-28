#!/usr/bin/env python2
import sys
import serial
import requests

class Arduino(object):
	def __init__(self, port, serial=serial):
		self.status = None

		try:
			self.serial = serial.Serial(port=port)
			self.serial.flushInput()
			self.serial.flushOutput()

			while True:
				print(self.serial.readline()
		except:
			"Failed to connect!"

		if self.serial.write("k") is 1:
			self.readStatus()

	def readStatus(self):
		self.status = self.serial.readline()

	def getStatus(self):
		return self.status

	def getDoorState(self):
		status = self.getStatus()
		print status
		status = status.replace("\r\n", "").split(",")
		door_state = "1" if (int(status[1]) > 150) else "0"

		return door_state

	def getTemperature(self):
		# dirty hack because of electrical problems
		status = self.getStatus()
		print status
		status = status.replace("\r\n", "").split(",")
		temperature = int(status[0]) - 12

		return temperature

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

arduino = Arduino(port)

status = arduino.getStatus()

#poster = Poster()
#poster.post_door_state(base_url, arduino.getDoorState(), security_token)
#poster.post_temperature(base_url, arduino.getTemperature(), security_token)