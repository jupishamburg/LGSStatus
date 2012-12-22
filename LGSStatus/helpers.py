import tweepy, random
from LGSStatus import cur, config

def connectToTwitter():
	auth = tweepy.OAuthHandler(config["twitter"]["consumer-key"], config["twitter"]["consumer-secret"])
	auth.set_access_token(config["twitter"]["access-token"], config["twitter"]["access-secret"])
	
	return tweepy.API(auth)

def getTypeVals(type, limit):
	out = "["
	
	# get all the data
	cur.execute("SELECT * FROM {0} ORDER BY time DESC LIMIT {1};".format(
		type,
		limit
	))
	
	# reverse it and put it into one string
	for d in reversed(cur.fetchall()):
		out += "[{0}, {1}],".format(
			d[2]*1000,
			d[1]
		)
	
	# delete the last comma, add a closing ] and return all the things
	return out[0:-1] + "]"

def getLastVal(type):
	# get the data
	cur.execute("SELECT * FROM {0} ORDER BY time DESC LIMIT 1;".format(
		type
	))
	
	# return!
	return cur.fetchone()

def doorTweet():
	from LGSStatus import twitter
	
	# get the last two door states
	cur.execute("SELECT * FROM door ORDER BY time DESC LIMIT 2;")
	states = cur.fetchall()
	
	if states[0][1] != states[1][1]:
		# check what to tweet - door opened
		if states[0][1] > states[1][1]:
			# get one random opening tweet and tweet it
			twitter.update_status(random.choice(config["twitter"]["tweets"]["opened"]))
		# '' - door closed
		else:
			twitter.update_status(random.choice(config["twitter"]["tweets"]["closed"]))
