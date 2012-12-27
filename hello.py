import cherrypy

class OnePage(object):
	def index(self):
		return "One page."

	def thing(self):
		return "Things"

	index.exposed = True
	thing.exposed = True

class Root:
	onepage = OnePage()

	def index(self):
		html = open("index.html", "r").read()
		return html
	index.exposed = True

cherrypy.quickstart(Root())