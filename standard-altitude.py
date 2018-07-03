################################################################################
#                                                                              #
#                        Aerodynamic Variable Calculator                       #
#                         Written by Johnathan Nicolosi                        #
#                             Created June 9, 2018                             #
#                                                                              #
################################################################################

import matplotlib.pyplot as plt

################################################################################
#                                                                              #
#           Variables and constants used for aerodynamic calculations          #
#                                                                              #
################################################################################

# Altitude in feet from sea level to 100000 ft
altitude = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,
            10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000,
            50000, 55000, 60000, 65000, 70000, 75000, 80000,
            85000, 90000, 95000, 100000]

# Temperature in degrees Ceslsius from sea level to 100000 ft
temperature = [15.0, 13.0, 11.0, 9.1, 7.1, 5.1, 3.1, 1.1, -0.9, -2.8,
               -4.8, -14.7, -24.6, -34.5, -44.4, -54.3, -56.5, -56.5,
               -56.5, -56.5, -56.5, -56.5, -56.5, -56.5, -56.5,
               -53.8, -49.2, -44.6, -40.1]

# Temperature in degrees Kelvin from sea level to 100000 ft
temp_kelvin = [288.15, 286.15, 284.15, 282.25, 280.25, 278.25, 276.25, 274.25, 272.25, 270.35, 268.35, 258.45, 248.55,
               238.65, 228.75, 218.85, 216.65, 216.65, 216.65, 216.65, 216.65, 216.65, 216.65, 216.65, 216.65, 219.35,
               223.96, 228.55, 233.05]

# Armospheric pressure, measured in bars from sea level to 100000 ft
pressure = [101325, 97773, 94322, 90971, 87718, 84560, 81494, 78520, 75634, 72835, 70121, 57752, 46575, 37757, 30346,
            24163, 18799, 14854, 11737, 9132, 7218, 5705, 4440, 3566, 2776, 2163, 1746, 1374, 1086]

# Density of air from sea level to 100000 ft
density = [1.2250, 1.1901, 1.1560, 1.1226, 1.09, 1.0581, 1.0269, 0.9965, 0.9667, 0.9377, 0.9093, 0.777, 0.6528, 0.5508,
           0.4615, 0.3837, 0.3023, 0.2388, 0.1887, 0.1468, 0.1161, 0.092, 0.071, 0.057, 0.045, 0.034, 0.0272, 0.02097,
           0.0162]

# Speed of sound, measured in knots, from sea level to 100000 ft
speed_sound = [661.7, 659.5, 657.2, 654.9, 652.6, 650.3, 647.9, 645.6, 643.3, 640.9, 638.6, 626.7, 614.6, 602.2, 589.5,
               576.6, 573.8, 573.8, 573.8, 573.8, 573.8, 573.8, 573.8, 573.8, 573.8, 577.4, 583.4, 589.3, 595.2]

temp_sea_level = temp_kelvin[0]
temp_ratio = [x / temp_sea_level for x in temp_kelvin]

atmospheric_gases = ['Nitrogen', 'Oxygen', 'Water', 'Argon', 'Carbon Dioxide', 'Neon', 'Helium', 'Methane', 'Krypton',
                     'Hydrogen', 'Nitrous Oxide', 'Xenon', 'Ozone', 'Particles', 'Iodine', 'Nitrogen Dioxide',
                     'Chlorofluorocarbons']
atmospheric_percent_volume = [78.08, 20.95, 4, 0.93, 0.036, 0.0018, 0.0005, 0.00017, 0.00014, 0.00005, 0.00003, 0.000009,
                              0.000004, 0.000001, 0.000002, 0.00000002]

print("""
####################################################################################################
#                                                                                                  #
#                                 Aerodynamic Variable Calculator                                  #
#                                  Written by Johnathan Nicolosi                                   #
#                                       Created June 9, 2018                                       #
#                                                                                                  #
####################################################################################################


""")

# User input data
mps = int(input("Enter velocity of flying object (meters per second): "))
user_altitude = int(input("Enter altitude of flying object (meters): "))
altitude_meters = user_altitude

meters_knots = mps * 1.94384
true_airspeed = meters_knots
mach_number = [true_airspeed / x for x in speed_sound]
mach = mach_number
regimes = ['Subsonic', 'Transonic', 'Supersonic', 'Hypersonic']
meter_foot_conversion = altitude_meters * 3.28084 # Converts from meters to feet
mps_mph_conversion = mps * 2.23694 # Converts from mps to mph
mps_knots_conversion = mps * 1.94384 # Converts from mps to knots

master_list = [
    ["Altitude", "Temperature", "Pressure   ", "Density ", "Speed of Sound", "Mach Number" ],
    [meter_foot_conversion, "(ft)", temp_kelvin[0], "(K)", pressure[0], "(Pa)", density[0], "(d)", speed_sound[0], "(a)", "%.1f" % mach_number[0], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[1], "(K)", pressure[1], "(Pa)", density[1], "(d)", speed_sound[1], "(a)", "%.1f" % mach_number[1], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[2], "(K)", pressure[2], "(Pa)", density[2], "(d)", speed_sound[2], "(a)", "%.1f" % mach_number[2], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[3], "(K)", pressure[3], "(Pa)", density[3], "(d)", speed_sound[3], "(a)", "%.1f" % mach_number[3], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[4], "(K)", pressure[4], "(Pa)", density[4], "(d)", speed_sound[4], "(a)", "%.1f" % mach_number[4], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[5], "(K)", pressure[5], "(Pa)", density[5], "(d)", speed_sound[5], "(a)", "%.1f" % mach_number[5], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[6], "(K)", pressure[6], "(Pa)", density[6], "(d)", speed_sound[6], "(a)", "%.1f" % mach_number[6], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[7], "(K)", pressure[7], "(Pa)", density[7], "(d)", speed_sound[7], "(a)", "%.1f" % mach_number[7], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[8], "(K)", pressure[8], "(Pa)", density[8], "(d)", speed_sound[8], "(a)", "%.1f" % mach_number[8], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[9], "(K)", pressure[9], "(Pa)", density[9], "(d)", speed_sound[9], "(a)", "%.1f" % mach_number[9], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[10], "(K)", pressure[10], "(Pa)", density[10], "(d)", speed_sound[10], "(a)", "%.1f" % mach_number[10], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[11], "(K)", pressure[11], "(Pa)", density[11], "(d)", speed_sound[11], "(a)", "%.1f" % mach_number[11], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[12], "(K)", pressure[12], "(Pa)", density[12], "(d)", speed_sound[12], "(a)", "%.1f" % mach_number[12], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[13], "(K)", pressure[13], "(Pa)", density[13], "(d)", speed_sound[13], "(a)", "%.1f" % mach_number[13], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[14], "(K)", pressure[14], "(Pa)", density[14], "(d)", speed_sound[14], "(a)", "%.1f" % mach_number[14], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[15], "(K)", pressure[15], "(Pa)", density[15], "(d)", speed_sound[15], "(a)", "%.1f" % mach_number[15], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[16], "(K)", pressure[16], "(Pa)", density[16], "(d)", speed_sound[16], "(a)", "%.1f" % mach_number[16], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[17], "(K)", pressure[17], "(Pa)", density[17], "(d)", speed_sound[17], "(a)", "%.1f" % mach_number[17], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[18], "(K)", pressure[18], "(Pa)", density[18], "(d)", speed_sound[18], "(a)", "%.1f" % mach_number[18], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[19], "(K)", pressure[19], "(Pa)", density[19], "(d)", speed_sound[19], "(a)", "%.1f" % mach_number[19], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[20], "(K)", pressure[20], "(Pa)", density[20], "(d)", speed_sound[20], "(a)", "%.1f" % mach_number[20], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[21], "(K)", pressure[21], "(Pa)", density[21], "(d)", speed_sound[21], "(a)", "%.1f" % mach_number[21], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[22], "(K)", pressure[22], "(Pa)", density[22], "(d)", speed_sound[22], "(a)", "%.1f" % mach_number[22], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[23], "(K)", pressure[23], "(Pa)", density[23], "(d)", speed_sound[23], "(a)", "%.1f" % mach_number[23], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[24], "(K)", pressure[24], "(Pa)", density[24], "(d)", speed_sound[24], "(a)", "%.1f" % mach_number[24], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[25], "(K)", pressure[25], "(Pa)", density[25], "(d)", speed_sound[25], "(a)", "%.1f" % mach_number[25], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[26], "(K)", pressure[26], "(Pa)", density[26], "(d)", speed_sound[26], "(a)", "%.1f" % mach_number[26], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[27], "(K)", pressure[27], "(Pa)", density[27], "(d)", speed_sound[27], "(a)", "%.1f" % mach_number[27], "(M)"],
    [meter_foot_conversion, "(ft)", temp_kelvin[28], "(K)", pressure[28], "(Pa)", density[28], "(d)", speed_sound[28], "(a)", "%.1f" % mach_number[28], "(M)"]
]

atmospheric_layers = ['Exosphere', 'Thermosphere', 'Mesosphere', 'Stratosphere', 'Troposphere']
cloud_type = ['Cirrocumulus', 'Cirrostratus', 'Cirrus', 'Altostratus', 'Altocumulus', 'Nimbostratus', 'Cumulonimbus',
              'Cumulus', 'Stratus', 'no']

ionospheric_layer = ['F Layer', 'E Layer', 'D Layer']
f_layer = [150000, 500000]
e_layer = [88000, 144000]
d_layer = [40000, 87000]

################################################################################
#                                                                              #
#                         Display aerodynamic variables                        #
#                                                                              #
################################################################################
print("")
print("""
####################################################################################################
#                                                                                                  #
#                                       Aerodynamic Variables                                      #
#                                                                                                  #
####################################################################################################
    """)

print("Altitude: ", "%.0f" % user_altitude, "meters (", "%.0f" % meter_foot_conversion, "ft )")
print("Velocity: ", "%.0f" % mps, "meters per second (", "%.0f" % mps_mph_conversion, "mph,",
      "%.0f" % mps_knots_conversion, "knots)")
print("")

print("""
####################################################################################################
#                                                                                                  #
#                                       Atmospheric Variables                                      #
#                                                                                                  #
####################################################################################################
    """)

print("")
if meter_foot_conversion >= 100000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[28], "K")
    print("Pressure:", "%.0f" % pressure[28], "Pa")
    print("Density:", "%.4f" % density[28], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[28], "a")
    print("Mach Number:", "%.1f" % mach_number[28], "M")

elif meter_foot_conversion >= 95000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[27], "K")
    print("Pressure:", "%.0f" % pressure[27], "Pa")
    print("Density:", "%.4f" % density[27], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[27], "a")
    print("Mach Number:", "%.1f" % mach_number[27], "M")

elif meter_foot_conversion >= 90000:
    print("Altitude: ",  " % .0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[26], "K")
    print("Pressure:", "%.0f" % pressure[26], "Pa")
    print("Density:", "%.4f" % density[26], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[26], "a")
    print("Mach Number:", "%.1f" % mach_number[26], "M")

elif meter_foot_conversion >= 85000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[25], "K")
    print("Pressure:", "%.0f" % pressure[25], "Pa")
    print("Density:", "%.4f" % density[25], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[25], "a")
    print("Mach Number:", "%.1f" % mach_number[25], "M")

elif meter_foot_conversion >= 80000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[24], "K")
    print("Pressure:", "%.0f" % pressure[24], "Pa")
    print("Density:", "%.4f" % density[24], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[24], "a")
    print("Mach Number:", "%.1f" % mach_number[24], "M")

elif meter_foot_conversion >= 75000:
    print("Altitude: ",  " %.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[23], "K")
    print("Pressure:", "%.0f" % pressure[23], "Pa")
    print("Density:", "%.4f" % density[23], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[23], "a")
    print("Mach Number:", "%.1f" % mach_number[23], "M")

elif meter_foot_conversion >= 70000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[22], "K")
    print("Pressure:", "%.0f" % pressure[22], "Pa")
    print("Density:", "%.4f" % density[22], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[22], "a")
    print("Mach Number:", "%.1f" % mach_number[22], "M")

elif meter_foot_conversion >= 65000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[21], "K")
    print("Pressure:", "%.0f" % pressure[21], "Pa")
    print("Density:", "%.4f" % density[21], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[21], "a")
    print("Mach Number:", "%.1f" % mach_number[21], "M")

elif meter_foot_conversion >= 60000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[20], "K")
    print("Pressure:", "%.0f" % pressure[20], "Pa")
    print("Density:", "%.4f" % density[20], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[20], "a")
    print("Mach Number:", "%.1f" % mach_number[20], "M")

elif meter_foot_conversion >= 55000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[19], "K")
    print("Pressure:", "%.0f" % pressure[19], "Pa")
    print("Density:", "%.4f" % density[19], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[19], "a")
    print("Mach Number:", "%.1f" % mach_number[19], "M")

elif meter_foot_conversion >= 50000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[18], "K")
    print("Pressure:", "%.0f" % pressure[18], "Pa")
    print("Density:", "%.4f" % density[18], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[18], "a")
    print("Mach Number:", "%.1f" % mach_number[18], "M")

elif meter_foot_conversion >= 45000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[17], "K")
    print("Pressure:", "%.0f" % pressure[17], "Pa")
    print("Density:", "%.4f" % density[17], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[17], "a")
    print("Mach Number:", "%.1f" % mach_number[17], "M")

elif meter_foot_conversion >= 40000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[16], "K")
    print("Pressure:", "%.0f" % pressure[16], "Pa")
    print("Density:", "%.4f" % density[16], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[17], "a")
    print("Mach Number:", "%.1f" % mach_number[16], "M")

elif meter_foot_conversion >= 35000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[15], "K")
    print("Pressure:", "%.0f" % pressure[15], "Pa")
    print("Density:", "%.4f" % density[15], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[15], "a")
    print("Mach Number:", "%.1f" % mach_number[15], "M")

elif meter_foot_conversion >= 30000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[14], "K")
    print("Pressure:", "%.0f" % pressure[14], "Pa")
    print("Density:", "%.4f" % density[14], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[14], "a")
    print("Mach Number:", "%.1f" % mach_number[14], "M")

elif meter_foot_conversion >= 25000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[13], "K")
    print("Pressure:", "%.0f" % pressure[13], "Pa")
    print("Density:", "%.4f" % density[13], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[13], "a")
    print("Mach Number:", "%.1f" % mach_number[13], "M")

elif meter_foot_conversion >= 20000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[12], "K")
    print("Pressure:", "%.0f" % pressure[12], "Pa")
    print("Density:", "%.4f" % density[12], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[12], "a")
    print("Mach Number:", "%.1f" % mach_number[12], "M")

elif meter_foot_conversion >= 15000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[11], "K")
    print("Pressure:", "%.0f" % pressure[11], "Pa")
    print("Density:", "%.4f" % density[11], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[11], "a")
    print("Mach Number:", "%.1f" % mach_number[11], "M")

elif meter_foot_conversion >= 10000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[10], "K")
    print("Pressure:", "%.0f" % pressure[10], "Pa")
    print("Density:", "%.4f" % density[10], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[10], "a")
    print("Mach Number:", "%.1f" % mach_number[10], "M")

elif meter_foot_conversion >= 9000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[9], "K")
    print("Pressure:", "%.0f" % pressure[9], "Pa")
    print("Density:", "%.4f" % density[9], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[9], "a")
    print("Mach Number:", "%.1f" % mach_number[9], "M")

elif meter_foot_conversion >= 8000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[8], "K")
    print("Pressure:", "%.0f" % pressure[8], "Pa")
    print("Density:", "%.4f" % density[8], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[8], "a")
    print("Mach Number:", "%.1f" % mach_number[8], "M")

elif meter_foot_conversion >= 7000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[7], "K")
    print("Pressure:", "%.0f" % pressure[7], "Pa")
    print("Density:", "%.4f" % density[7], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[7], "a")
    print("Mach Number:", "%.1f" % mach_number[7], "M")

elif meter_foot_conversion >= 6000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[6], "K")
    print("Pressure:", "%.0f" % pressure[6], "Pa")
    print("Density:", "%.4f" % density[6], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[6], "a")
    print("Mach Number:", "%.1f" % mach_number[6], "M")

elif meter_foot_conversion >= 5000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[5], "K")
    print("Pressure:", "%.0f" % pressure[5], "Pa")
    print("Density:", "%.4f" % density[5], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[5], "a")
    print("Mach Number:", "%.1f" % mach_number[5], "M")

elif meter_foot_conversion >= 4000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[4], "K")
    print("Pressure:", "%.0f" % pressure[4], "Pa")
    print("Density:", "%.4f" % density[4], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[4], "a")
    print("Mach Number:", "%.1f" % mach_number[4], "M")

elif meter_foot_conversion >= 3000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[3], "K")
    print("Pressure:", "%.0f" % pressure[3], "Pa")
    print("Density:", "%.4f" % density[3], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[3], "a")
    print("Mach Number:", "%.1f" % mach_number[3], "M")

elif meter_foot_conversion >= 2000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[2], "K")
    print("Pressure:", "%.0f" % pressure[2], "Pa")
    print("Density:", "%.4f" % density[2], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[2], "a")
    print("Mach Number:", "%.1f" % mach_number[2], "M")

elif meter_foot_conversion >= 1000:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[1], "K")
    print("Pressure:", "%.0f" % pressure[1], "Pa")
    print("Density:", "%.4f" % density[1], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[1], "a")
    print("Mach Number:", "%.1f" % mach_number[1], "M")

elif meter_foot_conversion >= 0:
    print("Altitude:", "%.0f" % user_altitude, "meters (", meter_foot_conversion, "ft )")
    print("Temperature:", "%.0f" % temp_kelvin[0], "K")
    print("Pressure:", "%.0f" % pressure[0], "Pa")
    print("Density:", "%.4f" % density[0], "d")
    print("Speed of Sound:", "%.1f" % speed_sound[0], "a")
    print("Mach Number:", "%.1f" % mach_number[0], "M")
    print("")

# This section will display the atmospheric layer the flying object is located in (based on user input)
if user_altitude < 190000000 and user_altitude >= 525000:
    print("The object is currently located in the", atmospheric_layers[0])
elif user_altitude < 525000 and user_altitude >= 80000:
    print("The object is currently located in the", atmospheric_layers[1])
elif user_altitude < 80000 and user_altitude >= 50000:
    print("The object is currently located in the", atmospheric_layers[2])
elif user_altitude < 50000 and user_altitude >= 13000:
    print("The object is currently located in the", atmospheric_layers[3])
elif user_altitude < 13000 and user_altitude > 0:
    print("The object is currently located in the", atmospheric_layers[4])
else:
    print("The object is not located within Earth's atmosphere")

# This section will list the types of clouds appearing at this altitude
if user_altitude >= 46000:
    print("There are", cloud_type[9], "clouds at this altitude.")
elif user_altitude >= 45000:
    print("At this altitude there are", cloud_type[0], "clouds,", cloud_type[1], "clouds and", cloud_type[2], "clouds.")
elif user_altitude >= 16500:
    print("At this altitude there are", cloud_type[3], "clouds.")
elif user_altitude >= 15000:
    print("At this altitude there are", cloud_type[4], "clouds.")
elif user_altitude >= 10000:
    print("At this altitude there are", cloud_type[5], "clouds,", cloud_type[6], "clouds, and", cloud_type[7], "clouds.")
elif user_altitude >= 3000:
    print("At this altitude there are", cloud_type[8], "clouds.")
elif user_altitude < 3000:
    print("Cloud formation does not occur at this altitude.")

# Display ionospheric layer
if user_altitude >= 500000:
    print("At this altitude there are no gas molecules to ionize")
elif user_altitude < 500000 and user_altitude >= 150000:
    print("The uppermost layer of the ionosphere (", ionospheric_layer[0], ") is divided into two layers: F1 and F2 Layers.")
elif user_altitude <= 444000 and user_altitude >= 88000:
    print("The second layer of the ionosphere (", ionospheric_layer[1], ") reflects radio waves with little to no cost "
                                                                          "and is vital for long-distance communications.")
elif user_altitude < 87000 and user_altitude > 40000:
    print("The bottom-most layer of the ionosphere (", ionospheric_layer[2], ") is characterized by relatively weak ionization.")
else:
    print("Molecules are too densly packed for ionization to occur at this altitude.")

# Include the Van Allen radiation belts
radiation_belts = ['Outer Radiation Belt', 'Inner Radiation Belt']
if user_altitude > 15000000 and user_altitude < 24400000:
    print("The object is currently located within the", radiation_belts[0])
elif user_altitude > 1000000 and user_altitude < 4500000:
    print("The object is currently located within the", radiation_belts[1])
else:
    print("")

#for item in master_list:
#    print(item, "   ")


################################################################################
#                                                                              #
#     Plot Temperature, Pressure, and Density at standard altitude (in feet)   #
#                                                                              #
################################################################################

# Figure 1: Standard Altitude Parameters
plt.figure(1)
plt.subplot(211)
plt.title('Standard Altitude')
plt.plot(temperature, altitude)
plt.ylabel('Altitude (ft)')
plt.xlabel('Temperature (C)')
plt.grid(True)

plt.subplot(212)
plt.ylabel('Altitude (ft)')
plt.xlabel('Speed of Sound (Knots)')
plt.plot(speed_sound, altitude)
plt.grid(True)

# Mach Number is calculated by dividing the object's velocity by the speed of sound
plt.figure(2)
plt.subplot(211)
plt.title('Mach Number Vs Temperature Ratio')
plt.plot(mach_number, altitude)
plt.ylabel('Altitude (ft)')
plt.xlabel('Mach Number')
plt.grid(True)

plt.subplot(212)
plt.plot(temp_ratio, altitude)
plt.ylabel('Altitude (ft)')
plt.xlabel('Temperature Ratio')
plt.grid(True)

# Air pressure and density decreases with altitude
plt.figure(3)
plt.subplot(211)
plt.title('Pressure Vs Density')
plt.plot(pressure, altitude)
plt.ylabel('Altitude (ft)')
plt.xlabel('Pressure (Pa)')
plt.grid(True)

plt.subplot(212)
plt.plot(density, altitude)
plt.ylabel('Altitude (ft)')
plt.xlabel('Density')
plt.grid(True)


plt.show()