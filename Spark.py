##
## Spark
## A shiny object that races around the screen.
##
class Spark(object):
	# init
	def __init__(self, strip):
		self.x = 8
		self.y = 8
		self.colorCycler = ColorCycler(self.strip.frameRate, [(255.0, 0.0, 0.0), (0.0, 0.0, 255.0)])
		self.radius = 2.0

		self.direction = 0.0
		self.speed = 1.0 / self.strip.frameRate
		return


	def run(self, strip):
		self.colorCycler.cycle()

		dx = math.sin(self.direction) * self.speed
		dy = math.cos(self.direction) * self.speed

		self.x += dx
		self.y += dy

		strip.drawBall(self.x, self.y, self.radius, self.colorCycler.currentColor)
		return
