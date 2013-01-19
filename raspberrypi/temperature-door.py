#!/usr/bin/env python2
import serial, time, sys, requests
def postDoorState(baseUrl, doorState, securityToken):
	params = {
	'value': doorState,
	'key': securityToken
	}
	requests.post(baseUrl + "/door", params)
def postTemperature(baseUrl, temperature, securityToken):
	params = {
	'value': temperature,
	'key': securityToken
	}
	requests.post(baseUrl + "/temperature", params)

# TODO: This should be mockable
if True:
	baseUrl = sys.argv[1]
	securityToken = sys.argv[2]
	port = sys.argv[3]

	s = serial.Serial(port=port)
	s.flushInput()
	s.flushOutput()

	# get the key-pair from the arduino
	if s.write("k") is 1:
		v = s.readline().replace("\r\n", "").split(",")

	doorState = "1" if (int(v[1]) > 150) else "0"
	temperature = int(v[0]) - 12 # dirty hack because of electrical problems
else:
	#Temporary Mock
	print "Should not be run on live server :D"
	baseUrl = "http://0.0.0.0:8080/append"
	doorState = "1"
	temperature = "52"
	securityToken = "ieSohc0oochie6Reequungoo7quoza8NuRaing9una"

postDoorState(baseUrl, doorState, securityToken)
postTemperature(baseUrl, temperature, securityToken)
