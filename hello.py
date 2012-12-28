import cherrypy
import os

class OnePage(object):
	def index(self):
		return "One page."

	def thing(self):
		return "Things"

	index.exposed = True
	thing.exposed = True

class Signup(object):
	def index(self):
		pass

class Root:
	onepage = OnePage()

	def index(self):
		html = open(os.path.join("static", "index.html"), "r").read()
		return html
	index.exposed = True

cherrypy.config.update("hello.config")
cherrypy.quickstart(Root())