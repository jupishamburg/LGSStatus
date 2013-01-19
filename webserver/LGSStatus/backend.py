import bottle, time
from LGSStatus import app, config, cur, db, helpers

@app.route("/append/<type>")
def insert(type):
	if not bottle.request.query.key in config["keys"]:
		bottle.abort(403, "Security token not given")

	if type not in config["types"]:
		bottle.abort(400, "what about correct types?")


	if not bottle.request.query.value:
		bottle.abort(400, "you think nobody needs the value? then i can't agree with you.")

	cur.execute("INSERT INTO {0} (value, time) VALUES (?, ?);".format(type), (
		bottle.request.query.value,
		int(time.time())
	))
	db.commit()

	# door tweet thingy
	if type == "door":
		helpers.doorTweet()

	return "1"