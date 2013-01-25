import unittest, json, unicodedata
class TestTweets(unittest.TestCase):
	def setUp(self):
		self.closed_door_hashtag = "#LGSgeschlossen"
		self.open_door_hashtag = "#LGSoffen"

		self.config = json.loads(open("tweets.json", "r").read(), "utf-8")
		self.tweets_for_open_door = self.config["tweets"]["opened"]
		self.tweets_for_closed_door = self.config["tweets"]["closed"]
		
	def test_tweets_not_having_over_140_chars(self):
		for tweet in self.tweets_for_open_door:
			tweet = unicodedata.normalize("NFC", tweet)
			self.assertTrue(len(tweet) <= 140, tweet.encode('utf-8') + " " + str(len(tweet)))

		for tweet in self.tweets_for_open_door:
			tweet = unicodedata.normalize("NFC", tweet)
			self.assertTrue(len(tweet) <= 140, tweet.encode('utf-8') + " " + str(len(tweet)))

	def test_closed_tweets_contain_hashtag(self):
		for tweet in self.tweets_for_closed_door:
			self.assertTrue(self.closed_door_hashtag in tweet, tweet)
			
	def test_open_tweets_contain_hash(self):
		for tweet in self.tweets_for_open_door:
			self.assertTrue(self.open_door_hashtag in tweet, tweet)
			
	if __name__ == '__main__':
		unittest.main(verbosity = 2)
