#!/usr/bin/env python2
from arduino import Arduino
from poster import Poster
import time
import sys
import subprocess
import json

if __name__ == '__main__':
	with open("config.json") as config_fh:
		config = json.load(config_fh)

	base_url = config["URL"]
	security_token = config["KEY"]
	port = config["TTY"]

	arduino = Arduino(port=port)
	arduino.start()

	while True:
		time.sleep(5)

		is_door_open = arduino.is_door_open()
		temperature = arduino.get_temperature()

		nmap = subprocess.Popen("./networkClientsInNetwork.sh", stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		network_clients_count = int(nmap.stdout.readlines()[0])

		print arduino.is_door_open()
		print arduino.get_temperature()
		print network_clients_count

		poster = Poster()
		poster.post_door_state(base_url, arduino.is_door_open(), security_token)
		poster.post_temperature(base_url, str(arduino.get_temperature()), security_token)
		poster.post_clients(base_url, str(network_clients_count), security_token)