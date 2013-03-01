#!/usr/bin/env python2
from arduino import Arduino
from poster import Poster
import time
import sys

if __name__ == '__main__':
	try:
		base_url = sys.argv[1]
		security_token = sys.argv[2]
		port = sys.argv[3]
	except IndexError:
		print "No arguments given, dummy run"
		pass

	arduino = Arduino(port=port)
	arduino.start()

	time.sleep(1)

	print arduino.getLastRecieved()
	is_door_open = arduino.is_door_open()
	temperature = arduino.get_temperature()

	poster = Poster()
	poster.post_door_state(base_url, arduino.is_door_open(), security_token)
	poster.post_temperature(base_url, str(arduino.get_temperature()), security_token)