#!/usr/bin/env python2
import serial, urllib2, time, sys

url = sys.argv[1]
key = sys.argv[2]
port = sys.argv[3]

s = serial.Serial(port=port)
s.flushInput()
s.flushOutput()

## get the key-pair from the arduino
if s.write("k") is 1:
	v = s.readline().replace("\r\n", "").split(",")

## door
state = 0
if int(v[1]) > 150:
	state = 1

print urllib2.urlopen("{0}/door?key={1}&value={2}".format(
	url,
	key,
	state
)).read()

## temperature (first: dirty hack because of electrical problems)
temp = int(v[0]) - 12
print urllib2.urlopen("{0}/temperature?key={1}&value={2}".format(
	url,
	key,
	temp
)).read()
