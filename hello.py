import cherrypy
import os
import database
from database import Session, User

top = open(os.path.join("static", "top.html"), "r").read()
bottom = open(os.path.join("static", "bottom.html"), "r").read()

class AllUsers(object):
	def index(self):
		tableText = "<div class=\"container\">\n\
			<table class=\"table\">\n\
				<thead>\n\
					<tr>\n\
						<th>Name</th>\n\
						<th>Username</th>\n\
						<th>Password</th>\n\
					</tr>\n\
				</thead>\n\
				<tbody>\n"
		session = Session()
		for user in session.query(User).order_by(User.id):
			tableText += ("<tr>\n<td>" + user.fullname + "</td>\n" +
			"<td>" + user.username + "</td>\n" +
			"<td>" + user.password + "</td>\n</tr>\n")

		tableText += "</tbody>\n</table>\n"
		session.close()
		return top + tableText + bottom

	index.exposed = True

class Signup(object):
	def index(self, fullname=None, username=None, password=None):
		if cherrypy.request.method == "POST":
			session = Session()
			new_user = User(username, fullname, password)
			session.add(new_user)
			session.commit()
			session.close()

		raise cherrypy.HTTPRedirect("/")

	index.exposed = True

class Root:
	allusers = AllUsers()
	signup = Signup()

	def index(self):
		html = open(os.path.join("static", "index.html"), "r").read()
		return top + html + bottom

	index.exposed = True

cherrypy.quickstart(Root(), config="hello.config")