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
	"-prod",
	"--productive-system",
	help="Run with this flag on productive live server.",
	action='store_true',
	required=False
)

parser.add_argument(
	"-ip",
	"--host-ip",
	help="Local IP on which the server will be listening",
	default="0.0.0.0"
)

parser.add_argument(
	"-p",
	"--port",
	help="Local port on which the server will be listening.",
	default="8080"
)

parser.add_argument(
	"-srv",
	"--server",
	help="Server to be used",
	default="tornado"
)


args = vars(parser.parse_args())

print args



import bottle
from LGSStatus import app, twitter

if (args['force_status_tweet_on_start'] is True):
	print("Force Tweet about Door State")
	twitter.tweet_door_state()

if __name__ == "__main__":
	bottle.run(app, host=args['host_ip'], port=args['port'], server=args['server'])
