import time, sqlite3

class DatabaseManager(object):
	def __init__(self, config):
		self.conn = sqlite3.connect(config)
		self.cur = self.conn.cursor()

	def get_last_two_door_states(self):
		self.cur.execute("SELECT * FROM door ORDER BY time DESC LIMIT 2;")
		states = self.cur.fetchall()
		
		return states

	def get_type_values(self, type, limit):
		out = "["
		self.cur.execute("SELECT * FROM {0} ORDER BY time DESC LIMIT {1};".format(
			type,
			limit
		))

		# Reverse order
		for d in reversed(self.cur.fetchall()):
			out += "[{0}, {1}],".format(
				d[2]*1000,
				d[1]
			)

		# delete the last comma
		return out[0:-1] + "]"

	def get_current_value(self, type):
		self.cur.execute("SELECT * FROM {0} ORDER BY time DESC LIMIT 1;".format(
			type
		))

		return self.cur.fetchone()

	def is_door_open(self):
		if self.was_door_state_updated_within_last_hour():
			return self.get_current_value("door")[1] == True

	def set_value_of_type(self, type, value):
		self.cur.execute("INSERT INTO {0} (value, time) VALUES (?, ?);".format(type), (
			value,
			int(time.time())
		))

		self.conn.commit()

	def get_last_door_timestamp(self):
		self.cur.execute("SELECT time FROM door ORDER BY ID DESC LIMIT 1;")

		for row in self.cur:
			self.timestamp = row[0]

		return self.timestamp

	def was_door_state_updated_within_last_hour(self):
		current_time = time.time()
		last_update_time = self.get_last_door_timestamp()
		diff = current_time - last_update_time

		return diff < 3600

	def __del__(self):
		self.conn.close()