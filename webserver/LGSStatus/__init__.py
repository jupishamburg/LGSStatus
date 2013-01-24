import bottle, sqlite3, json
from LGSStatus import db_manager, twitter_handler

with open("config.json") as config_fh:
	config = json.load(config_fh)

with open("tweets.json") as tweets_fh:
	tweets = json.load(tweets_fh)

db = sqlite3.connect(config["db"])
db_manager = db_manager.DatabaseManager(db)
app = bottle.Bottle()

bottle.TEMPLATE_PATH.append("./LGSStatus/templates")

twitter = twitter_handler.TwitterHandler(config, tweets, db_manager)

bash_command = "sass --watch ./LGSStatus/static/css/lgsstatus.sass:./LGSStatus/static/css/lgsstatus.css"
import subprocess
process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)

@app.route("/static/<filepath:path>")
def static(filepath):
	return bottle.static_file(filepath, root="./LGSStatus/static")

import LGSStatus.frontend
import LGSStatus.backend

