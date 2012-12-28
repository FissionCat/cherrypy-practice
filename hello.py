import cherrypy
import os
import database
from database import Session, User

class OnePage(object):
	def index(self):
		return "One page."

	def thing(self):
		return "Things"

	index.exposed = True
	thing.exposed = True

class Signup(object):
	def index(self, fullname=None, username=None, password=None):
		if cherrypy.request.method == "POST":
			session = Session()
			new_user = User(username, fullname, password)
			session.add(new_user)
			session.commit()
			session.close()

	index.exposed = True

class Root:
	onepage = OnePage()
	signup = Signup()

	def index(self):
		html = open(os.path.join("static", "index.html"), "r").read()
		return html
	index.exposed = True

cherrypy.quickstart(Root(), config="hello.config")