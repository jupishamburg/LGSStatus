import bottle, sqlite3

config = {
	"db": "lgs.db",
	
	"types": [
		"door",
		"clients",
		"temperature"
	],
	"keys": [
		"ieSohc0oochie6Reequungoo7quoza8NuRaing9una"
	]
}

db = sqlite3.connect(config["db"])
cur = db.cursor()
app = bottle.Bottle()

bottle.TEMPLATE_PATH.append("./LGSStatus/templates")

@app.route("/static/<filepath:path>")
def static(filepath):
	return bottle.static_file(filepath, root="./LGSStatus/static")

import LGSStatus.frontend
import LGSStatus.backend
