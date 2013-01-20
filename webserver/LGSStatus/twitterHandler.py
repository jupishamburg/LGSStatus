import tweepy, random

class TwitterHandler(object):
	def __init__(self, config, dbManager):
		self.config = config
		self.dbManager = dbManager

		auth = tweepy.OAuthHandler(self.config["twitter"]["consumer-key"], config["twitter"]["consumer-secret"])
		auth.set_access_token(self.config["twitter"]["access-token"], config["twitter"]["access-secret"])

		self.tweepy = tweepy.API(auth)

	def tweetAboutDoorStateIfChanged(self):
		self._setLastTwoDoorStates()
		if self._doorStateHasChanged():
			if self._doorIsOpen():
				self.tweepy.update_status(random.choice(self.config["twitter"]["tweets"]["opened"]))
			else:
				self.tweepy.update_status(random.choice(self.config["twitter"]["tweets"]["closed"]))

	def _setLastTwoDoorStates(self):
		self.states = dbManager.getLastTwoDoorStates()

	def _doorStateHasChanged(self):
		return self.states[0][1] != self.states[1][1]

	def _doorIsOpen(self):
		return self.states[0][1] > self.states[1][1]