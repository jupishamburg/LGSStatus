import bottle
from LGSStatus import app, twitterHandler, dbManager

@app.route("/")
def index():
	dataOfToday = {
		"clients":dbManager.getTypeValues("clients", 300),
		"temperature":dbManager.getTypeValues("temperature", 300),
		"door":dbManager.getTypeValues("door", 300)
	}

	return bottle.jinja2_template(
		"index.html",
		dataOfToday = dataOfToday,
		isDoorOpen = dbManager.isDoorOpen()
	)
