import bottle, datetime
from LGSStatus import app, db, watch

@app.route("/")
def index():
	data_of_today = {
		"clients": db.get_type_values("clients", 300),
		"temperature": db.get_type_values("temperature", 300),
		"door": db.get_type_values("door", 300)
	}

	return bottle.jinja2_template(
		"index.html",
		data_of_today = data_of_today,
		is_door_open = db.is_door_open(),
		last_updated = datetime.datetime.fromtimestamp(db.get_last_door_timestamp()).strftime("%d.%m.%Y %H:%M"),
		is_kaput = not db.was_door_state_updated_within_last_hour()
	)

@app.get("/meta-status")
def meta_status():
	watch.check_if_kaput()
	return bottle.jinja2_template(
		"meta_status.html",
		is_kaput = watch._is_kaput()
	)