import bottle
from LGSStatus import app, helpers

@app.route("/")
def index():
	day = {
		"clients":		helpers.getTypeVals("clients", 300),
		"temperature":	helpers.getTypeVals("temperature", 300),
		"door":			helpers.getTypeVals("door", 300)
	}
	
	# get the current door state
	if helpers.getLastVal("door")[1] == True:
		current = '<i style="color:#A0B046;" class="icon-asterisk"></i> offen.'
	else:
		current = '<i style="color:#F24E4E;" class="icon-ban-circle"></i> zu.'

	return bottle.jinja2_template("index.html", day=day, current=current)
