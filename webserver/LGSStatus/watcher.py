from threading import Timer
from LGSStatus import db_manager

class Watcher(object):
	def __init__(self, twitter, db_config, db_manager=db_manager, timer=Timer):
		self.timer = timer
		self.config = db_config
		self.twitter = twitter
		self.status = "working"
		self.watcher_interval = 2 * 60 * 60
		self.db = None

		self.check_if_kaput(db_manager)

	def check_if_kaput(self, db_manager=db_manager):
		if not self._is_kaput():
			# New Instance as same Sqlite connection  cannot be shared between threads
			self.db = self.getDb(db_manager, self.config)
			if not self.db.was_door_state_updated_within_last_hour():
				self._set_status_to_kaput()
				self.twitter.tweet_status_unknown()

		self.timer(self.watcher_interval, self.check_if_kaput).start()
		print "fnord"

	def getDb(self, db_manager, config):
		return db_manager.DatabaseManager(config)

	def set_status_to_working(self):
		self.status = "working"

	def _set_status_to_kaput(self):
		self.status = "kaput"

	def _is_kaput(self):
		return self.status == "kaput"

import mock
class DevWatcher(Watcher):
	def __init__(self, twitter, db_config, db_manager=db_manager, timer=mock.Mock):
		super(DevWatcher, self)