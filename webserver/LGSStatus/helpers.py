import tweepy, random
from LGSStatus import db, config

def connectToTwitter():
	auth = tweepy.OAuthHandler(config["twitter"]["consumer-key"], config["twitter"]["consumer-secret"])
	auth.set_access_token(config["twitter"]["access-token"], config["twitter"]["access-secret"])
	
	return tweepy.API(auth)
def doorTweet():
	from LGSStatus import twitter, dbManager
	states = dbManager.getLastTwoDoorStates()
	if states[0][1] != states[1][1]:
		# check what to tweet - door opened
		if states[0][1] > states[1][1]:
			# get one random opening tweet and tweet it
			twitter.update_status(random.choice(config["twitter"]["tweets"]["opened"]))
		# '' - door closed
		else:
			twitter.update_status(random.choice(config["twitter"]["tweets"]["closed"]))
