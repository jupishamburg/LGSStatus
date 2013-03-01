from threading import Thread
import serial
import random
import time

class Arduino(Thread):
	def __init__(self, port):
		Thread.__init__(self, target=self.recieve)
		self.daemon = True
		self.last_recieved = None

		self.serial = self.configure_port(port)
		self.serial.open()

	def configure_port(self, port_id):
		ser = serial.Serial(port=port_id, timeout=1)
		ser.rtscts = True
		ser.dsrdtr = True

		return ser

	def recieve(self):
		while True:
			self.serial.flushInput()
			self.serial.flushOutput()
			if self.serial.isOpen():
				self.last_recieved = self.serial.readline().replace("\r\n", "").split("|")

	def getLastRecieved(self):
		return self.last_recieved

	def getStatus(self):
		return self.status

#	def getDoorState(self):
#		val = self.getDataArray()
#		door_state = "1" if (int(val[1]) > 150) else "0"
#
#		print door_state
#		return door_state
#
#	def getTemperature(self):
#		# dirty hack because of electrical problems
#		val = self.getDataArray()
#		temperature = int(val[0]) - 12
#
#		print temperature
#		return temperature