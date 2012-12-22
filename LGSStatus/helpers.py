from LGSStatus import cur

def getTypeVals(type, limit):
	out = "["
	
	# get all the data
	cur.execute("SELECT * FROM {0} ORDER BY time DESC LIMIT {1};".format(
		type,
		limit
	))
	
	# reverse it and put it into one string
	for d in reversed(cur.fetchall()):
		out += "[{0}, {1}],".format(
			d[2]*1000,
			d[1]
		)
	
	# delete the last comma, add a closing ] and return all the things
	return out[0:-1] + "]"

def getLastVal(type):
	# get the data
	cur.execute("SELECT * FROM {0} ORDER BY time DESC LIMIT 1;".format(
		type
	))
	
	# return!
	return cur.fetchone()
