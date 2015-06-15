__author__ = 'Daniel'
import cherrypy

class Testing:

    def index(self):
        return "This is the Index"
    index.exposed = True

    def hello(self, string, num2):
        return string + " =) " + num2
    # to run input this
    # hello?string=stringtest&num2=lalala

    hello.exposed = True

cherrypy.quickstart(Testing())
