import bottle, time
from LGSStatus import app, config, cur, db

@app.route("/append/<type>")
def insert(type):
	# key check
	if bottle.request.query.key in config["keys"]:
		# type check
		if type in config["types"]:
			# value check
			if bottle.request.query.value:
				try:
					cur.execute("INSERT INTO {0} (value, time) VALUES (?, ?);".format(type), (
						bottle.request.query.value,
						int(time.time())
					))
					db.commit()
					
					return "1"
				except:
					bottle.abort(400, "interesting value ... but it's not the right data type for this type.")
			
			bottle.abort(400, "you think nobody needs the value? then i can't agree with you.")
		bottle.abort(400, "what about correct types?")
	bottle.abort(403, "muhahaha penis")
