import os
import re
from string import letters

import jinja2
import webapp2

from google.appengine.ext import db

html_dir = os.path.join(os.path.dirname(__file__), 'html')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(html_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class HomePage(Handler):
	def get(self):
		self.render("home.html")

class Portfolio(Handler):
	def get(self):
		self.render("portfolio.html")

class About(Handler):
    def get(self):
        self.render("about.html")

app = webapp2.WSGIApplication([('/', HomePage),
                                ('/portfolio', Portfolio),
                                ('/about', About)],
                              debug = True)
