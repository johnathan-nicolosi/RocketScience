##############################################
#                                            #
#           NOAA Satellite Tracker           #
#         Using Python and Pyorbital         #
#                                            #
#       Written by: Johnathan Nicolosi       #
#                12 OCT 2018                 #
#                                            #
##############################################
#
# To install PyOrbital on Linux: 
# $ sudo apt_get install python_pyorbital
#
from pyorbital import tlefile
from pyorbital.orbital import Orbital
from datetime import datetime

# There are two ways we can track orbital elements using PyOrbital

# First we will use the TLE files created using tle_web_scraper.py 
# Dont forget to change the file path to the actual location of the saved TLE files
tle = tlefile.read('NOAA 20 [+]', '/path/to/tle/files/noaa_tle_file.txt')
print tle

# The second method uses current TLEs from the internet, which we do not need to download
orb = Orbital("NOAA 20") # For additional satellites, subsitute "NOAA 20" with other NOAA satellites (numbered 1 - 20)
now = datetime.utcnow()

# Get normalized position and velocity of the satellite
current_position = orb.get_position(now)
print(current_position)

# Get the longitude, latitude and altitude of the satellite
current_lonlatalt = orb.get_lonlatalt(now)
print(current_lonlatalt)

# Get the orbit number of the satellite
current_orbit_number = orb.get_orbit_number(now, tbus_style=False)
print("Current orbit:", current_orbit_number)

