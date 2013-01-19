#!/usr/bin/env python2
import serial, urllib, urllib2, time, sys

def main():
	url = sys.argv[1]
	securityToken = sys.argv[2]
	port = sys.argv[3]

	s = serial.Serial(port=port)
	s.flushInput()
	s.flushOutput()

	## get the key-pair from the arduino
	if s.write("k") is 1:
		v = s.readline().replace("\r\n", "").split(",")

	doorState = True if (int(v[1]) > 150) else False
	postDoorState(url, doorState, securityToken)

	temperature = int(v[0]) - 12 # dirty hack because of electrical problems
	postTemperature(url, temperature, securityToken)

def postDoorState(url, doorState, securityToken):
	params = {
	'value': doorState,
	'key': securityToken
	}
	URLRequest(url + "/door", params, "POST")

def postTemperature(url, temperature, securityToken):
	params = {
	'value': temperature,
	'key': securityToken
	}
	URLRequest(url + "/temperature", params, "POST")

def URLRequest(url, params, method="GET"):
	if method == "POST":
		return urllib2.Request(url, data=urllib.urlencode(params))
	else:
		return urllib2.Request(url + "?" + urllib.urlencode(params))

if __name__ == "__main__":
	main()