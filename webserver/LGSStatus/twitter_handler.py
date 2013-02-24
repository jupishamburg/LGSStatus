import tweepy, random

class TwitterHandler(object):
	def __init__(self, config, tweets, db_manager):
		self.config = config
		self.tweets = tweets
		self.db_manager = db_manager

		auth = tweepy.OAuthHandler(self.config["twitter"]["consumer-key"], config["twitter"]["consumer-secret"])
		auth.set_access_token(self.config["twitter"]["access-token"], config["twitter"]["access-secret"])

		self.tweepy = tweepy.API(auth)
		self.last_tweeted = None

	def tweet_about_door_state_if_changed(self):
		self.last_two_door_states = self.db_manager.get_last_two_door_states()
		if self._door_state_has_changed():
			self.tweet_door_state()

	def tweet_door_state(self):
		if self._door_is_open():
			self.tweet_door_is_open()
		else:
			self.tweet_door_is_closed()

	def tweet_door_is_open(self):
		self.tweet(random.choice(self.tweets["tweets"]["opened"]), "open")

	def tweet_door_is_closed(self):
		self.tweet(random.choice(self.tweets["tweets"]["closed"]), "closed")

	def tweet_status_unknown(self):
		self.tweet("Technische Probleme. Status der LGS ist unbekannt :(", "kaput")

	def tweet(self, message, last_tweeted = None):
		try:
			self.tweepy.update_status(message)
			self.last_tweeted = last_tweeted
		except Exception:
			#TODO: Some Exception handling that is not this obsolete :D
			pass

	def _door_state_has_changed(self):
		return self.last_two_door_states[0][1] != self.last_two_door_states[1][1]

	def _door_is_open(self):
		return self.db_manager.is_door_open()