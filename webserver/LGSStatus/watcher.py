import time
from threading import Timer

class Watcher(object):
	def __init__(self, db_manager, twitter):
		self.db_manager = db_manager
		self.twitter = twitter
		self.status = "working"
		self.watcher_interval = 2 * 60 * 60

		self.check_if_kaput()

	def check_if_kaput(self):
		if not self._is_kaput():
			if not self.was_door_state_updated_within_last_hour():
				self._set_status_to_kaput()
				try:
					self.twitter.tweet_status_unknown()
				except Exception:
					pass
		Timer(self.watcher_interval, self.check_if_kaput).start()

	def set_status_to_working(self):
		self.status = "working"

	def _set_status_to_kaput(self):
		self.status = "kaput"

	def _is_kaput(self):
		return self.status == "kaput"

	def was_door_state_updated_within_last_hour(self):
		current_time = time.time()
		last_update_time = self.db_manager.get_last_door_timestamp()
		diff = current_time - last_update_time

		return diff < 3600