import requests

class Poster(object):
	def __init__(self, requests=requests):
		self.requests=requests

	def post_door_state(self, base_url, door_state, security_token):

		if door_state is None:
			raise ValueError

		door_state = "1" if door_state else "0"

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

	def post_clients(self, base_url, network_clients_count, security_token):
		params = {
			'value': network_clients_count,
			'key': security_token
		}

		self.requests.post(base_url + "/clients", params)