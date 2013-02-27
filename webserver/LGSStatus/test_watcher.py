from LGSStatus import watcher, twitter, db
import unittest, mock
from mock import call

class TestWatcher(unittest.TestCase):
	def setUp(self):
		self.twitterMock = mock.MagicMock()
		self.dbConfigMock = mock.MagicMock()
		self.dbManagerMock = mock.MagicMock()
		self.timerMock = mock.MagicMock()

	def test_status_is_working_on_start(self):
		testWatcher = self.newTestInstance()
		self.assertFalse(testWatcher._is_kaput())

	def test_run_timer(self):
		testWatcher = self.newTestInstance()
		testWatcher.getDb = mock.Mock(testWatcher.getDb, return_value=self.dbManagerMock)

		self.timerMock.assert_has_calls(call().start())

	def test_tweet_status_unknown_on_broken(self):
		testWatcher = self.newTestInstance()
		self.dbManagerMock.was_door_state_updated_within_last_hour.return_value = False
		testWatcher.getDb = mock.Mock(testWatcher.getDb, return_value=self.dbManagerMock)
		testWatcher._is_kaput = mock.Mock(testWatcher._is_kaput, return_value = False)
		testWatcher.check_if_kaput()

		self.twitterMock.tweet_status_unknown.assert_called_once_with()
		self.assertEqual(testWatcher.status, "kaput")

		self.resetMocks()

	def newTestInstance(self):
		return watcher.Watcher(twitter=self.twitterMock, db_config=self.dbConfigMock, db_manager=self.dbManagerMock, timer=self.timerMock)

	def resetMocks(self):
		self.twitterMock = mock.MagicMock()
		self.dbConfigMock = mock.MagicMock()
		self.dbManagerMock = mock.MagicMock()
		self.timerMock = mock.MagicMock()