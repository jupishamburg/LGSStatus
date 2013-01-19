import bottle
from LGSStatus import app, helpers

@app.route("/")
def index():
	dataOfToday = {
		"clients":		helpers.getTypeVals("clients", 300),
		"temperature":	helpers.getTypeVals("temperature", 300),
		"door":			helpers.getTypeVals("door", 300)
	}

	isDoorOpen = (helpers.getLastVal("door")[1] == True)

	return bottle.jinja2_template("index.html", dataOfToday=dataOfToday, isDoorOpen=isDoorOpen)
