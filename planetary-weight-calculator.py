###################################################################
#                                                                 #
# Planetary Weight Calculator                                     #
#                                                                 #
# Calculate you weight on each planet, including the moon and sun #
#                                                                 #
# Written by Johnathan Nicolosi                                   #
#                                                                 #
###################################################################

#universal gravitational constant
G = 6.67408 * 10**-11 #Newton-meter^2/kilogram^2

#The mass for each celestial body (in kilograms)
mass_earth = 5.98 * 10**24
mass_mercury = 3.30 * 10**23
mass_venus = 4.87 * 10**24
mass_mars = 6.42 * 10**23
mass_jupiter = 1.90 * 10**27
mass_saturn = 5.69 * 10**26
mass_uranus = 8.68 * 10**25
mass_neptune = 1.02 * 10**26
mass_sun = 1.99 * 10**30
mass_moon = 7.35 * 10**22

#The radius of each celestial body (in kilometers)
radius_earth = 6378 * 10**3
radius_mercury = 2439 * 10**3
radius_venus = 6051 * 10**3
radius_mars = 3393 * 10**3
radius_jupiter = 71492 * 10**3
radius_saturn = 60268 * 10**3
radius_uranus = 25559 * 10**3
radius_neptune = 24764 * 10**3
radius_sun = 696000 * 10**3
radius_moon = 1738 * 10**3

#The gravitational acceleration vector of each celestial body (in Newtons)
gravity_earth = G * mass_earth / radius_earth**2
gravity_mercury = G * mass_mercury / radius_mercury**2
gravity_venus = G * mass_venus / radius_venus**2
gravity_mars = G * mass_mars / radius_mars**2
gravity_jupiter = G * mass_jupiter / radius_jupiter**2
gravity_saturn = G * mass_saturn / radius_saturn**2
gravity_uranus = G * mass_uranus / radius_uranus**2
gravity_neptune = G * mass_neptune / radius_neptune**2
gravity_sun = G * mass_sun / radius_sun**2
gravity_moon = G * mass_moon / radius_moon**2

print("Determine your weight on each planet")
normal_weight = float(input("Enter your weight in pounds (lbs):"))
print("")
mass = normal_weight / 9.8
weight_earth = mass * gravity_earth
print("Your mass is:", "%.2f" % mass, "kg")
print("")
print("Your weight on Earth is:", "%.0f" % weight_earth, "lbs")
weight_mercury = mass * gravity_mercury
print("Your weight on Mercury is:", "%.0f" % weight_mercury, "lbs")
weight_venus = mass * gravity_venus
print("Your weight on Venus is:", "%.0f" % weight_venus, "lbs")
weight_mars = mass * gravity_mars
print("Your weight on Mars is:", "%.0f" % weight_mars, "lbs")
weight_jupiter = mass * gravity_jupiter
print("Your weight on Jupiter is:", "%.0f" % weight_jupiter, "lbs")
weight_saturn = mass * gravity_saturn
print("Your weight on Saturn is:", "%.0f" % weight_saturn, "lbs")
weight_uranus = mass * gravity_uranus
print("Your weight on Uranus is:", "%.0f" % weight_uranus, "lbs")
weight_neptune = mass * gravity_neptune
print("Your weight on Neptune is:", "%.0f" % weight_neptune, "lbs")
weight_sun = mass * gravity_sun
print("Your weight on the Sun is:", "%.0f" % weight_sun, "lbs")
weight_moon = mass * gravity_moon
print("Your weight on the Moon is:", "%.0f" % weight_moon, "lbs")