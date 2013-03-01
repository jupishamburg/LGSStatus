#!/usr/bin/env python2
from arduino import Arduino
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

	while True:
		print arduino.getLastRecieved()
		time.sleep(1)

#	print 'frak this:'
#	print arduino.getStatus()
#	print arduino.getDoorState()
#	print arduino.getTemperature()
#
#	poster = Poster()
#	poster.post_door_state(base_url, arduino.getDoorState(), security_token)
#	poster.post_temperature(base_url, arduino.getTemperature(), security_token)