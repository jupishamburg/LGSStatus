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

	def is_door_open(self):
		try:
			lumen = int(self.getLastRecieved()[1])
			return_val = lumen > 150
		except Exception:
			return_val = None

		return return_val

	def get_temperature(self):
		try:
			temperature = int(float(self.getLastRecieved()[0]))
			temperature_offset = -5
			return_val = int(temperature) + temperature_offset
		except Exception:
			return_val = None
			pass

		return return_val