import unittest, json, unicodedata
class TestTweets(unittest.TestCase):
	def setUp(self):
		self.closedDoorHash = "#LGSgeschlossen"
		self.openDoorHash = "#LGSoffen"

		self.config = json.loads(open("tweets.json", "r").read(), "utf-8")
		self.doorOpenTweets = self.config["tweets"]["opened"]
		self.doorClosedTweets = self.config["tweets"]["closed"]
		
	def test_tweets_not_over_140_digits(self):
		for tweet in self.doorOpenTweets:
			tweet = unicodedata.normalize("NFC", tweet)
			self.assertTrue(len(tweet) <= 140, tweet.encode('utf-8') + " " + str(len(tweet)))

		for tweet in self.doorOpenTweets:
			tweet = unicodedata.normalize("NFC", tweet)
			self.assertTrue(len(tweet) <= 140, tweet.encode('utf-8') + " " + str(len(tweet)))

	def test_closed_tweets_contain_hash(self):
		for tweet in self.doorClosedTweets:
			self.assertTrue(self.closedDoorHash in tweet, tweet)
			
	def test_open_tweets_contain_hash(self):
		for tweet in self.doorOpenTweets:
			self.assertTrue(self.openDoorHash in tweet, tweet)
			
	if __name__ == '__main__':
		unittest.main(verbosity=2)
