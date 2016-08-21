from TPack import TPack
from TBike import TBike


# Pick what configuration we're in
conf = 1		# Pack
conf = 2		# Bike

# Options
dimmer = 0



# Let's do it
if conf == 1:
	pack = TPack(dimmer, 1)
	pack.run()
elif conf == 2:
	bike = TBike(dimmer)
	bike.run()
