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
import datetime

# To add current date to file extension
dt = str(datetime.date.today())

###################################################################################################################################
#                                                                                                                                 #
# We will pull two-line element data for the NOAA and GOES weather tracking satellites as well as the International Space Station #
#                                                                                                                                 #
###################################################################################################################################


# Let us begin by pulling TLE data for all of the Geostationary Operational Environmental Satellite (GOES)
# Request data from www.celestrack.com
def goes_tle():
    html = requests.get("https://www.celestrak.com/NORAD/elements/goes.txt").text
    soup = BeautifulSoup(html, 'html5lib')
    # Convert data to string
    goes_tle = str(html)
    # opens TLE file and overwrites old data with current data
    goes = open('tle_files/goes/goes_tle_'+dt+'.txt', 'w')
    # Writes tle data as a string to the open text file
    goes.write(goes_tle)
    goes.close()
goes_tle()

# Next we will pull TLE data for all of the Polar Operational Environmental Satellites (POES/NOAA)
# Request data from www.celestrack.com
def noaa_tle():
    html = requests.get("https://www.celestrak.com/NORAD/elements/noaa.txt").text
    # Convert data to string
    noaa_tle = str(html)
    # opens TLE file and overwrites old data with current data
    noaa = open('tle_files/noaa/noaa_tle_'+dt+'.txt', 'w')
    # Writes tle data as a string to the open text file
    noaa.write(noaa_tle)
    noaa.close()
noaa_tle()

# Lastly we will pull TLE data on the International Space Station (ISS)
# Request data from www.celestrack.com
def iss_tle():
    html = requests.get("https://www.celestrak.com/satcat/tle.php?CATNR=25544").text
    soup = BeautifulSoup(html, 'html5lib')
    body = soup.pre.text
    # Convert data to string
    iss_tle = str(body)
    # opens TLE file and overwrites old data with current data
    iss = open('tle_files/iss/iss_tle_'+dt+'.txt', 'w')
    # Writes tle data as a string to the open text file
    iss.write(iss_tle)
    iss.close()
iss_tle()
