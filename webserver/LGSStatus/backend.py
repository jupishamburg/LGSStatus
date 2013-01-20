import bottle, time
from LGSStatus import app, config, dbManager, helpers

@app.post("/append/<type>")
def insert(type):
	securityKey = bottle.request.POST.key
	value = bottle.request.POST.value

	if securityKey not in config["keys"]:
		bottle.abort(401, "Security token not given")

	if type not in config["types"]:
		bottle.abort(400, "Invalid type")

	if not value:
		bottle.abort(400, "Missing value parameter")

	dbManager.setValueOfType(type, value)

	if type == "door":
		helpers.doorTweet()

	return type + ":" + value