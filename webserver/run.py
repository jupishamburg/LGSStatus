#!/usr/bin/env python2
from argparse import ArgumentParser

parser = ArgumentParser(description="LGS Status")
parser.add_argument(
	"-ft",
	"--force-status-tweet-on-start",
	help="Will force a tweet about current door state. May be helpful if last tweet was incorrect but next tweet would only be issued on door state change.",
	action='store_true',
	required=False
)

parser.add_argument(
	"-dev",
	"--dev",
	help="Dev mode",
	action='store_true',
	required=False
)

args = vars(parser.parse_args())

import bottle
from LGSStatus import app, twitter, config

if (args['force_status_tweet_on_start'] is True):
	print("Force Tweet about Door State")
	twitter.tweet_door_state()

if (args['dev'] is True):
	def pseudoTweet(message, mode):
		print(message)
		print(mode)

	twitter.tweet = pseudoTweet

if __name__ == "__main__":
	bottle.run(app, host="0.0.0.0", port="8080", server="tornado")
