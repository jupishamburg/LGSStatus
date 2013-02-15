import tweepy, random

class TwitterHandler(object):
	def __init__(self, config, tweets, db_manager):
		self.config = config
		self.tweets = tweets
		self.db_manager = db_manager

		auth = tweepy.OAuthHandler(self.config["twitter"]["consumer-key"], config["twitter"]["consumer-secret"])
		auth.set_access_token(self.config["twitter"]["access-token"], config["twitter"]["access-secret"])

		self.tweepy = tweepy.API(auth)

	def tweet_about_door_state_if_changed(self):
		self.last_two_door_states = self.db_manager.get_last_two_door_states()
		if self._door_state_has_changed():
			if self._door_is_open():
				self.tweepy.update_status(random.choice(self.tweets["tweets"]["opened"]))
			else:
				self.tweepy.update_status(random.choice(self.tweets["tweets"]["closed"]))

	def _door_state_has_changed(self):
		return self.last_two_door_states[0][1] != self.last_two_door_states[1][1]

	def _door_is_open(self):
		return self.last_two_door_states[0][1] > self.last_two_door_states[1][1]
