import bottle, json, sys
from LGSStatus import db_manager, watcher, twitter_handler

print 'oo'

try:
	is_dev_mode = not sys.modules['__main__'].args['productive_system']
except AttributeError:
	is_dev_mode = True

try:
	with open("config.json") as config_fh:
		config = json.load(config_fh)
except IOError:
	with open("config.json.example") as config_fh:
		config = json.load(config_fh)

with open("tweets.json") as tweets_fh:
	tweets = json.load(tweets_fh)

app = bottle.Bottle()
db = db_manager.DatabaseManager(config["db"])

if is_dev_mode:
	twitter = twitter_handler.DevTwitterHandler(config, tweets, db)
	watch = None
	#TODO: Make this not break tests!
	#watcher.DevWatcher(twitter, config["db"])
else:
	twitter = twitter_handler.TwitterHandler(config, tweets, db)
	watch = watcher.Watcher(twitter, config["db"])

bash_command = "sass --watch ./LGSStatus/static/css/lgsstatus.sass:./LGSStatus/static/css/lgsstatus.css"
import subprocess
try:
	process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
except OSError:
	print "Cannot convert sass to css!"
	pass

bottle.TEMPLATE_PATH.append("./LGSStatus/templates")

@app.route("/static/<filepath:path>")
def static(filepath):
	return bottle.static_file(filepath, root="./LGSStatus/static")

import LGSStatus.frontend
import LGSStatus.backend