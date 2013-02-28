import bottle
from LGSStatus import app, config, db, twitter, watch

@app.post("/append/<type>")
def insert(type):
	security_key = bottle.request.POST.key
	value = bottle.request.POST.value

	if security_key not in config["keys"]:
		bottle.abort(401, "Security token not given")

	if type not in config["types"]:
		bottle.abort(400, "Invalid type")

	if not value:
		bottle.abort(400, "Missing value parameter")

	db.set_value_of_type(type, value)

	if type == "door":
		twitter.tweet_about_door_state_if_changed()
		watch.set_status_to_working()

	return type + ":" + value
