###################################################################
#                                                                 #
# Universal Weight Calculator                                     #
#                                                                 #
# Calculate you weight on Mars at various altitudes               #
#                                                                 #
# Written by Johnathan Nicolosi                                   #
#                                                                 #
###################################################################


G = 6.67408 * 10**-11 #Universal gravitational constant
mass_mars = 6.42 * 10**23
radius_mars = 3393 * 10**3
gravity_mars = G * mass_mars / radius_mars**2

print("Calculate your weight at various altitudes on Mars")

normal_weight = float(input("Enter your normal weight on Earth:"))

mass = normal_weight / 9.8 #calculates mass based on weight given in pounds

altitude = float(input("Enter your altitude in kilometers:")) #altitude in kilometers above the Martian surface

distance_mars = radius_mars + (altitude * 1000) #calculates the distance from the center of Mars
gravity = G * mass_mars / distance_mars**2 #calculates gravitational acceleration based on the altitude given
calculated_weight = mass * gravity #calculates your weight at the altitude given

print("Your mass is:", "%.2f" % mass)
print("The gravitational force at this altitude is:", "%.2f" % gravity, "m/s^2")
print("Your weight at this altitude is:", "%.0f" % calculated_weight, "lbs")

