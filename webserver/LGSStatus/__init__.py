import bottle, sqlite3, json
from LGSStatus import dbManager, twitterHandler

config = json.loads(open("config.json", "r").read())
db = sqlite3.connect(config["db"])
dbManager = dbManager.DbManager(db)
app = bottle.Bottle()

bottle.TEMPLATE_PATH.append("./LGSStatus/templates")

twitter = twitterHandler.TwitterHandler(config, dbManager)

@app.route("/static/<filepath:path>")
def static(filepath):
	return bottle.static_file(filepath, root="./LGSStatus/static")

import LGSStatus.frontend
import LGSStatus.backend
