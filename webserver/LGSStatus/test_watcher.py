from LGSStatus import watcher, twitter, db
import unittest, mock

class TestWatcher(unittest.TestCase):
	def setUp(self):
		self.twitterMock = mock.MagicMock()
		self.dbConfigMock = mock.MagicMock()
		self.dbManagerMock = mock.MagicMock()
	def test_status_is_kaput_on_start(self):
		testWatcher = watcher.Watcher(twitter=self.twitterMock, db_config=self.dbConfigMock, db_manager=self.dbManagerMock)
		print testWatcher._is_kaput()
		self.assertFalse(testWatcher._is_kaput())

