##
## Spark
## A shiny object that races around the screen.
##
class Spark(object):
	# init
	def __init__(self):
		self.x = 8
		self.y = 8
		self.color = (128.0, 128.0, 0.0)
		self.radius = 2
		return


	def run(self, strip):
		strip.drawBall(self.x, self.y, self.radius, self.color)
		return
