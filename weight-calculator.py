###################################################################
#                                                                 #
# Universal Weight Calculator                                     #
#                                                                 #
# Calculate you weight on Earth at various altitudes              #
#                                                                 #
# Written by Johnathan Nicolosi                                   #
#                                                                 #
###################################################################
#
import math
#
G = 6.67408 * 10**-11 #Universal gravitational constant
mass_earth = 5.98 * 10**24 # mass of Earth in kilograms
distance_surface = 6.378 * 10**6 #distance from center of Earth to its surface, in kilometers
#
print("Calculate your weight at various altitudes on Earth")
#
normal_weight = float(input("Enter your weight in pounds:"))
#
mass = normal_weight / 9.8 #calculates mass based on weight given in pounds
#
altitude = float(input("Enter your altitude in meters:"))
#
distance_earth = distance_surface + (altitude * 1000) #calculates the distance from the center of the earth
gravity = G * mass_earth / distance_earth**2 #calculates gravitational acceleration based on the altitude given
calculated_weight = mass * gravity #calculates your weight at the altitude given
v = math.sqrt(2 * gravity * altitude)
t = altitude / v
#
print("Your mass is:", "%.2f" % mass, "kg")
print("The gravitational force at this altitude is:", "%.2f" % gravity, "m/s^2")
print("Your weight at this altitude is:", "%.0f" % calculated_weight, "lbs")
print("Your initial velocity is:", "%.0f" % v, "m/s")
print("It will take", "%.0f" % t, "seconds to fall to Earth from this altitude.")


