import bottle
from LGSStatus import app, helpers, dbManager

@app.route("/")
def index():
	dataOfToday = {
		"clients":dbManager.getTypeVals("clients", 300),
		"temperature":dbManager.getTypeVals("temperature", 300),
		"door":dbManager.getTypeVals("door", 300)
	}

	isDoorOpen = (dbManager.getLastVal("door")[1] == True)

	return bottle.jinja2_template("index.html", dataOfToday=dataOfToday, isDoorOpen=isDoorOpen)
