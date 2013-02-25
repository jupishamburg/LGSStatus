from threading import Timer
from LGSStatus import db_manager

class Watcher(object):
	def __init__(self, twitter, db_config, db_manager=db_manager):
		self.config = db_config
		self.twitter = twitter
		self.status = "working"
		self.watcher_interval = 2 * 60 * 60
		self.db_manager = db_manager
		self.check_if_kaput()

	def check_if_kaput(self):
		if not self._is_kaput():
			# New Instance as same Sqlite connection  cannot be shared between threads
			db = self.db_manager.DatabaseManager(self.config)
			if not db.was_door_state_updated_within_last_hour():
				self._set_status_to_kaput()
				self.twitter.tweet_status_unknown()

		Timer(self.watcher_interval, self.check_if_kaput).start()

	def set_status_to_working(self):
		self.status = "working"

	def _set_status_to_kaput(self):
		self.status = "kaput"

	def _is_kaput(self):
		return self.status == "kaput"
