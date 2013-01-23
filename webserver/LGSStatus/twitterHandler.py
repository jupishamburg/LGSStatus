import tweepy, random

class TwitterHandler(object):
	def __init__(self, config, tweets, dbManager):
		self.config = config
		self.tweets = tweets
		self.dbManager = dbManager

		auth = tweepy.OAuthHandler(self.config["twitter"]["consumer-key"], config["twitter"]["consumer-secret"])
		auth.set_access_token(self.config["twitter"]["access-token"], config["twitter"]["access-secret"])

		self.tweepy = tweepy.API(auth)

	def tweetAboutDoorStateIfChanged(self):
		self.lastTwoDoorStates = self.dbManager.getLastTwoDoorStates()
		if self._doorStateHasChanged():
			if self._doorIsOpen():
				self.tweepy.update_status(random.choice(self.tweets["tweets"]["opened"]))
			else:
				self.tweepy.update_status(random.choice(self.tweets["tweets"]["closed"]))

	def _doorStateHasChanged(self):
		return self.lastTwoDoorStates[0][1] != self.lastTwoDoorStates[1][1]

	def _doorIsOpen(self):
		return self.lastTwoDoorStates[0][1] > self.lastTwoDoorStates[1][1]