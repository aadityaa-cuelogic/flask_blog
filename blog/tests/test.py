import unittest
import os
from .. import app

class BlogTest(unittest.TestCase):
	"""docstring for BlogTest"""
	def setUp(self):
		"""Execute before every test case"""
		app.config['TESTING'] = True
		self.app = app.test_client()

	def tearDown(self):
		"""Execute after every test case"""
		pass

	def test_Index_url(self):
		response = self.app.get("/")
		self.assertEqual(response.status_code, 200)