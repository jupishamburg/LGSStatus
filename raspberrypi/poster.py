import requests

class Poster(object):
	def __init__(self, requests=requests):
		self.requests=requests

	def post_door_state(self, base_url, door_state, security_token):
		params = {
		'value': door_state,
		'key': security_token
		}

		self.requests.post(base_url + "/door", params)

	def post_temperature(self, base_url, temperature, security_token):
		params = {
		'value': temperature,
		'key': security_token
		}

		self.requests.post(base_url + "/temperature", params)