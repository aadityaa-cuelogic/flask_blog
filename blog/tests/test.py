import unittest
import os
from .. import app, db
from ..forms import SignupForm, SigninForm

# import pdb;pdb.set_trace();

class BlogTest(unittest.TestCase):
	"""docstring for BlogTest"""
	def setUp(self):
		"""Execute before every test case"""
		app.config.from_object('config.TestConfig')
		self.app = app.test_client()
		self.app_context = app.test_request_context()
		self.app_context.push()
		db.create_all()

	def tearDown(self):
		"""Execute after every test case"""
		db.session.remove()
		db.drop_all()

	def test_Index_url(self):
		response = self.app.get("/")
		self.assertEqual(response.status_code, 200)

	def test_addUser_url(self):
		response = self.app.get("/adduser")
		self.assertEqual(response.status_code, 200)

	def test_signupform(self):
		data = {
			'name' : 'aditya',
			'email' : 'aditya@yopmail.com',
			'password' : 'password',
			'username' : 'aditya'
		}
		signupform = SignupForm(data=data)
		# print signupform.validate()
		# print signupform.errors
		self.assertTrue(signupform.validate(), True)

	def test_addUser_view(self):
		data = {
			'name' : 'aditya',
			'email' : 'aditya@yopmail.com',
			'password' : 'password',
			'username' : 'aditya'
		}
		# import pdb;pdb.set_trace();
		response = self.app.post("/adduser", data=data, follow_redirects=True)
		assert "User added successfully" in response.data

	def test_loginUser_view(self):
		data = {
			'name' : 'aditya',
			'email' : 'aditya@yopmail.com',
			'password' : 'password',
			'username' : 'aditya'
		}
		# import pdb;pdb.set_trace();
		response = self.app.post("/adduser", data=data, follow_redirects=True)
		if "User added successfully" in response.data:
			login_data = {
				'username':'aditya',
				'password':'password'
			}
			response = self.app.post("/login", data=data, follow_redirects=True)
		assert "Login Successful" in response.data