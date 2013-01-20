import time

class DbManager(object):
	def __init__(self, db):
		self.db = db
		self.dbcursor = db.cursor
		
	def getLastTwoDoorStates(self):
		self.dbcursor.execute("SELECT * FROM door ORDER BY time DESC LIMIT 2;")
		states = self.dbcursor.fetchall()
		
		return states
		
	def getTypeValues(self, type, limit):
		out = "["
		self.dbcursor.execute("SELECT * FROM {0} ORDER BY time DESC LIMIT {1};".format(
			type,
			limit
		))

		# Reverse order
		for d in reversed(self.dbcursor.fetchall()):
			out += "[{0}, {1}],".format(
				d[2]*1000,
				d[1]
			)

		# delete the last comma
		return out[0:-1] + "]"

	def getLastVal(self, type):
		self.dbcursor.execute("SELECT * FROM {0} ORDER BY time DESC LIMIT 1;".format(
			type
		))

		return self.dbcursor.fetchone()

	def setValueOfType(self, type, value):
		self.dbcursor.cur.execute("INSERT INTO {0} (value, time) VALUES (?, ?);".format(type), (
		value,
		int(time.time())
		))

		self.db.commit()
