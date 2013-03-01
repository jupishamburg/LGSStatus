#!/usr/bin/env python2
import sys
import serial
import requests

class Arduino(object):
	def __init__(self, port):
		self.status = None

		try:
			self.serial = self.configure_port(port)
		except:
			"Failed to connect!"

		if self.serial.inWaiting():
			self.status = self.serial.readline()

	def configure_port(port_id, serial=serial):
		ser = serial.Serial()
		ser.port = port_id
		ser.baudrate = 9600
		ser.rtscts = True
		ser.dsrdtr = True

		return ser

	def getStatus(self):
		return self.status

	def getDoorState(self):
		status = self.getStatus()
		status = self.status.replace("\r\n", "").split(",")
		door_state = "1" if (int(status[1]) > 150) else "0"

		return door_state

	def getTemperature(self):
		# dirty hack because of electrical problems
		self.status = self.getStatus()
		self.status = self.status.replace("\r\n", "").split(",")
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

def main():
	base_url = sys.argv[1]
	security_token = sys.argv[2]
	port = sys.argv[3]
	arduino = Arduino(port)

	status = arduino.getStatus()

	print 'frak this:'
	print arduino.getStatus()
	print arduino.getDoorState()
	print arduino.getTemperature()

	poster = Poster()
	poster.post_door_state(base_url, arduino.getDoorState(), security_token)
	poster.post_temperature(base_url, arduino.getTemperature(), security_token)

if __name__ == '__main__':
	try:
		main()
	except IndexError:
		print "Trying again ..."
		main()