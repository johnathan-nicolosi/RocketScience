#############################################
#                                           #
#        NORAD Two-Line Element Sets        #
#            Python Web Scraper             #
#                                           #
#      Written by: Johnathan Nicolosi       #
#                12 OCT 2018                #
#                                           #
#############################################


from bs4 import BeautifulSoup
import requests
soup= BeautifulSoup(html, 'html5lib')

###################################################################################################################################
#                                                                                                                                 #
# We will pull two-line element data for the NOAA and GOES weather tracking satellites as well as the International Space Station #
#                                                                                                                                 #
###################################################################################################################################


# Let us begin by pulling TLE data for all of the Geostationary Operational Environmental Satellite (GOES)
# Request data from www.celestrack.com
html = requests.get("https://www.celestrak.com/NORAD/elements/goes.txt").text
# Convert data to string
goes_tle = str(html)
# opens TLE file and overwrites old data with current data
goes = open('goes_tle_file.txt', 'w')
# Writes tle data as a string to the open text file
goes.write(goes_tle)
goes.close()

# Next we will pull TLE data for all of the Polar Operational Environmental Satellites (POES/NOAA)
# Request data from www.celestrack.com
html = requests.get("https://www.celestrak.com/NORAD/elements/noaa.txt").text
# Convert data to string
noaa_tle = str(html)
# opens TLE file and overwrites old data with current data
noaa = open('noaa_tle_file.txt', 'w')
# Writes tle data as a string to the open text file
noaa.write(noaa_tle)
noaa.close()

# Lastly we will pull TLE data on the International Space Station (ISS)
# Request data from www.celestrack.com
html = requests.get("https://www.celestrak.com/satcat/tle.php?CATNR=25544").text
body = soup.pre.text
# Convert data to string
iss_tle = str(body)
# opens TLE file and overwrites old data with current data
iss = open('iss_tle_file.txt', 'w')
# Writes tle data as a string to the open text file
iss.write(iss_tle)
iss.close()
