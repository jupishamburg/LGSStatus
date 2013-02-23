import time

class DatabaseManager(object):
	def __init__(self, db):
		self.db = db
		self.dbcursor = db.cursor()
		
	def get_last_two_door_states(self):
		self.dbcursor.execute("SELECT * FROM door ORDER BY time DESC LIMIT 2;")
		states = self.dbcursor.fetchall()
		
		return states
		
	def get_type_values(self, type, limit):
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

	def get_current_value(self, type):
		self.dbcursor.execute("SELECT * FROM {0} ORDER BY time DESC LIMIT 1;".format(
			type
		))

		return self.dbcursor.fetchone()

	def is_door_open(self):
		return self.get_current_value("door")[1] == True

	def set_value_of_type(self, type, value):
		self.dbcursor.execute("INSERT INTO {0} (value, time) VALUES (?, ?);".format(type), (
		value,
		int(time.time())
		))

		self.db.commit()

	def get_last_door_timestamp(self):
		self.dbcursor.execute("SELECT time FROM door ORDER BY ID DESC LIMIT 1;")

		for row in self.dbcursor:
			self.timestamp = row[0]

		return self.timestamp
