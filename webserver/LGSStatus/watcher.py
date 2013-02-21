import time
from threading import Timer, Thread

class Watcher(object):
	def __init__(self, db_manager, twitter):
		self.db_manager = db_manager
		self.twitter = twitter
		self.status = "working"
		self.watcher_intervall = 2 * 60 * 60

		self.check_if_kaputt()

	def check_if_kaputt(self):
		if not self._is_kaputt():
			if not self.was_door_state_updated_within_last_15_min():
				self._set_status_to_kaputt()
				self.twitter.tweet_status_unknown()

		Timer(self.watcher_intervall, self.check_if_kaputt).start()

	def set_status_to_working(self):
		self.status = "working"

	def _set_status_to_kaputt(self):
		self.status = "kaputt"

	def _is_kaputt(self):
		return (self.status == "kaputt")

	def was_door_state_updated_within_last_15_min(self):
		current_time = time.time()
		last_update_time = self.db_manager.get_last_door_timestamp()
		diff = current_time - last_update_time

		return diff < 900