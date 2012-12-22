import bottle, sqlite3, json

config = json.loads(open("config.json", "r").read())

db = sqlite3.connect(config["db"])
cur = db.cursor()
app = bottle.Bottle()

bottle.TEMPLATE_PATH.append("./LGSStatus/templates")

@app.route("/static/<filepath:path>")
def static(filepath):
	return bottle.static_file(filepath, root="./LGSStatus/static")

import LGSStatus.frontend
import LGSStatus.backend
