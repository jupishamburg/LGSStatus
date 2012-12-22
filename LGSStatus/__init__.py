import bottle, sqlite3

db = sqlite3.connect("lgs.db")
cur = db.cursor()
app = bottle.Bottle()

bottle.TEMPLATE_PATH.append("./LGSStatus/templates")

@app.route("/static/<filepath:path>")
def static(filepath):
	return bottle.static_file(filepath, root="./LGSStatus/static")

import LGSStatus.frontend
import LGSStatus.backend
