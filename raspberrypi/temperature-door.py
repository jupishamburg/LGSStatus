#!/usr/bin/env python2
import sys
import serial
import requests
import time
from threading import Thread
from threading import Lock
import random

class Arduino(Thread):
	def __init__(self, port):
		Thread.__init__(self, target=self.recieve)
		self.daemon = True
		self.last_recieved = None

		try:
			self.serial = self.configure_port(port)
		except:
			"Failed to connect!"
			import mock
			self.serial = mock.MagicMock()
			pass

	def configure_port(port_id, serial=serial):
		ser = serial.Serial(port_id, timeout=1)
		ser.port = port_id
		ser.rtscts = True
		ser.dsrdtr = True

		return ser

	def recieve(self):
		buffer = ''
		while True:
#			buffer = buffer + self.serial.read(self.serial.inWaiting())
#			if '\n' in buffer:
#				lines = buffer.split('\n') # Guaranteed to have at least 2 entries
#				self.last_recieved_lock.aquire()
#				self.last_received = lines[-2]
#				self.last_recieved_lock.release()
#				#If the Arduino sends lots of empty lines, you'll lose the
#				#last filled line, so you could make the above statement conditional
#				#like so: if lines[-2]: last_received = lines[-2]
#				buffer = lines[-1]

			self.last_recieved = random.Random().randint(0, 100)

	def getLastRecieved(self):
		return self.last_recieved



	def getStatus(self):
		return self.status

	def getDataArray(self):
		return self.getStatus().replace("\r\n", "").split(",")

#
#	def getDoorState(self):
#		val = self.getDataArray()
#		door_state = "1" if (int(val[1]) > 150) else "0"
#
#		print door_state
#		return door_state

#	def getTemperature(self):
#		# dirty hack because of electrical problems
#		val = self.getDataArray()
#		temperature = int(val[0]) - 12
#
#		print temperature
#		return temperature

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

#	print 'frak this:'
#	print arduino.getStatus()
#	print arduino.getDoorState()
#	print arduino.getTemperature()
#
#	poster = Poster()
#	poster.post_door_state(base_url, arduino.getDoorState(), security_token)
#	poster.post_temperature(base_url, arduino.getTemperature(), security_token)

if __name__ == '__main__':
	try:
		base_url = sys.argv[1]
		security_token = sys.argv[2]
		port = sys.argv[3]
	except IndexError:
		print "No arguments given, dummy run"
		pass

	arduino = Arduino(port='fnord')
	arduino.start()

	while True:
		print arduino.getLastRecieved()