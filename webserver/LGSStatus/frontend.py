import bottle
from LGSStatus import app, twitter_handler, db_manager

@app.route("/")
def index():
	data_of_today = {
		"clients": db_manager.get_type_values("clients", 300),
		"temperature": db_manager.get_type_values("temperature", 300),
		"door": db_manager.get_type_values("door", 300)
	}

	return bottle.jinja2_template(
		"index.html",
		data_of_today = data_of_today,
		is_door_open = db_manager.is_door_open()
	)
