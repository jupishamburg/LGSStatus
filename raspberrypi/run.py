#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from arduino import Arduino
from poster import Poster
from argparse import ArgumentParser
from termcolor import cprint
import time
import subprocess
import json

if __name__ == '__main__':
	is_live_run = None
	parser = ArgumentParser()

	parser.add_argument(
		"-prod",
		"--productive-system",
		help="When set, will continiously update the webserver. Otherwise dev enviroment is assumed.",
		action='store_true',
		required=False
	)

	args = vars(parser.parse_args())
	is_live_run = args["productive_system"]

	if is_live_run:
		cprint("Live run!", color="magenta")
	else:
		cprint("Test run!", color="green")

	with open("config.json") as config_fh:
		config = json.load(config_fh)

	base_url = config["URL"]
	security_token = config["KEY"]
	port = config["TTY"]

	arduino = Arduino(port=port)
	arduino.start()
	time.sleep(1)

	network_clients_count = None

	while True:
		is_door_open = arduino.is_door_open()
		temperature = arduino.get_temperature()

		if is_live_run:
			poster = Poster()
			poster.post_door_state(base_url, arduino.is_door_open(), security_token)
			poster.post_temperature(base_url, str(arduino.get_temperature()), security_token)
			poster.post_clients(base_url, str(network_clients_count), security_token)

			nmap = subprocess.Popen("./networkClientsInNetwork.sh", stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			network_clients_count = int(nmap.stdout.readlines()[0])
			time.sleep(10)
		else:
			time.sleep(2)

		cprint("Nmap " + str(network_clients_count), color="blue")
		cprint("Tür offen: " + str(arduino.is_door_open()), color="yellow")
		cprint("Temperatur: " + str(arduino.get_temperature()), color="cyan")