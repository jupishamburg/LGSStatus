from threading import Thread
import serial
import time

class Arduino(Thread):
	def __init__(self, port):
		Thread.__init__(self, target=self.recieve)
		self.daemon = True
		self.last_recieved = None

		self.serial = self.configure_port(port)
		self.serial.open()

		self.is_door_open = None
		self.temperature = None

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
				self.set_is_door_open(self.last_recieved )
				self.set_temperature(self.last_recieved)

	def get_last_recieved(self):
		return self.last_recieved

	def get_is_door_open(self):
		return self.is_door_open

	def get_temperature(self):
		return self.temperature

	def set_is_door_open(self, recieved):
		try:
			lumen = int(recieved[1])
			self.is_door_open = lumen > 150
		except Exception:
			self.is_door_open = None
			pass

	def set_temperature(self, recieved):
		try:
			temperature = int(float(recieved[0]))
			temperature_offset = -5
			self.temperature = int(temperature) + temperature_offset
		except Exception:
			self.temperature = None
			pass