#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import time, subprocess, json, datetime
from os import path
from arduino import Arduino
from poster import Poster
from argparse import ArgumentParser
from termcolor import cprint

def main():
	config_path = path.relpath("config.json")
	with open(config_path) as config_fh:
		config = json.load(config_fh)

	args = get_args()
	is_live_run = args["productive_system"]

	base_url = config["URL"]
	security_token = config["KEY"]
	port = config["TTY"]

	poster = Poster()
	if is_live_run:
		cprint("Live run!", color="magenta")
		delay = 300
	else:
		cprint("Test run!", color="green")
		delay = 3

	arduino = Arduino(port=port)
	arduino.start()
	time.sleep(15)

	network_clients_count = None

	while True:
		is_door_open = arduino.get_is_door_open()
		temperature = arduino.get_temperature()
		recieved = arduino.get_last_recieved()

		nmap = subprocess.Popen("./networkClientsInNetwork.sh", stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		network_clients_count = int(nmap.stdout.readlines()[0])

		poster.post_door_state(base_url, is_door_open, security_token)
		poster.post_temperature(base_url, str(temperature), security_token)
		poster.post_clients(base_url, str(network_clients_count), security_token)

		cprint(str(datetime.datetime.now().strftime('%G-%b-%d-%H:%M:%S')), color="red")
		cprint("Nmap " + str(network_clients_count), color="blue")
		cprint("Tür offen: " + str(is_door_open), color="yellow")
		cprint("Temperatur: " + str(temperature), color="cyan")
		print recieved
		print ("\n")

		time.sleep(delay)

def get_args():
	parser = ArgumentParser()
	parser.add_argument(
		"-prod",
		"--productive-system",
		help="When set, will continiously update the webserver. Otherwise dev enviroment is assumed.",
		action='store_true',
		required=False
	)

	return vars(parser.parse_args())

if __name__ == '__main__':
	main()