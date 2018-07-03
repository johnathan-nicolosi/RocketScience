###############################
#  Calculate Escape Velocity  #
#                             #
#Written by Johnathan Nicolosi#
#                             #
###############################
#
from Tkinter import *
from ttk import *
#
def gui():

  def result():
      Label(ev_frame, text='The amount of force behind an object equals the mass of the object and its rate of acceleration.').grid(column=1, row=1, sticky= W)
      Label(ev_frame, text='Therefore, massive objects moving at greater speeds have more force behind them than do smaller,slower-moving objects.').grid(column=1, row=2, sticky= W)
mass_payload=int(input("Enter the mass of the payload, in kilograms: "))
speed=float(input("Enter speed of object in meters per second: "))
time=1
acceleration = speed / time
force= mass_payload * acceleration
G=6.67408*10**-11 #Newtons
#
mass_earth=5.972*10**24 #kg
velocity_earth=30000
gravity_earth=9.8 #meters pers second squared
gravitational_constant_earth=3.98600 * 10**14 #m**3/sec^2
weight_earth=mass_payload * gravity_earth #kg
escape_velocity_earth=11200
escape_force_earth=mass_payload * escape_velocity_earth
#
mass_moon=7.34767309*10**22 #kg
velocity_moon=1000
gravity_moon=1.622
weight_moon=mass_payload * gravity_moon
distance_moon=384472282
relative_speed_moon=speed-velocity_moon
escape_velocity_moon=2380 #meters per second
earth_to_moon=15900
time_moon=distance_moon / relative_speed_moon #to calculate time to travel to the moon at current speed
time_moon_minutes=time_moon / 60 #to convert to minutes
time_moon_hours=time_moon_minutes / 60 #convert to hours
#
mass_mars=0.64171*10**24 #kg
gravity_mars=3.71
distance_mars=54600000000
velocity_mars=24100
relative_speed_mars=speed-velocity_mars
time_mars=distance_mars / relative_speed_mars #time to catc
time_mars_minutes=time_mars / 60 #Convert to minutes
time_mars_hours=time_mars_minutes / 60 #convert to hours
escape_velocity_mars=5030
earth_to_mars=21000 #meters per second
#
mass_ceres=9.39*10**20 #kg
escape_velocity_ceres=510
#
earth_to_venus=22000 #meters per sec
#
########################################################################################################################
print("Earth revolves around the sun at a speed of", velocity_earth, "meters per second and has a mass of ", mass_earth, "kg.")
print("The weight of the object while travelling at this speed will be approximately", weight_earth, "lbs")
print("The force behind that object will then be", force, "Newtons, or about", force / 9.81, "kg")
print("")
print("Newton's law of gravitation defines the attractional force Fg between two bodies as follows:\n"
      "Fg = Gm1m2/R^2\n"
      "Here G is gravitational constant of the universe (G = 6.670 x 10^-11m^3/kg-sec^2), m1 and m2 are the masses of the two attracting bodies,\n"
      "and R is the distance between their centers of mass. ")
print("With this knowledge, we can calculate the amount of force required for an object to break free of "
      "Earth's gravity. Earth's gravitational constant is the product of Newtons universal constant and earth's mass, m1 (5.974 * 10**24kg).\n"
      "Earth's gravitational constant = 3.98600 * 10**14m**3/sec**2")
print("")
print("In order to escape Earth's gravity, an object must travel at approximately",escape_velocity_earth, "km/s.")
print("Travelling at",escape_velocity_earth, "meters per second, the force behind the object will be", escape_force_earth, "Newtons.")
if (speed > escape_velocity_earth):
    print("At your current rate of ", speed, " m/sec, you should have no problem escaping Earth's gravitational field.")
else:
    print("At your current rate of ", speed, " m/sec, you will inevitably come back down to Earth.")
print("")
print("To achive low earth orbit, a spacecraft must accelerate to a speed of nearly 8050 meters per second.")
if (speed > 8050):
    print("At your current rate of ", speed, " m/sec, you should have no problem achieving low earth orbit.")
else:
    print("At your current rate of ", speed, " m/sec, you are not travelling fast enough to achieve low earth orbit.")
print("")
print("However, in order to reach the moon, the Apollo 10 spacecraft travelled at 11080 meters per second.")
print("The moon is travelling around the earth at a rate of", velocity_moon, "meters per second and has a mass of", mass_moon, "kg.")
print("Therefore, for every hour of spaceflight, the moon will have traveled", velocity_moon*3600, "meters.")
if (speed > earth_to_moon):
    print("At your current speed of", speed, "m/s, it will take approximately", time_moon, "seconds, or", time_moon / 3600, "hours to catch the moon.")
else:
    print("You are not travelling fast enouch to reach the moon.")
print("")
print("Mars is travelling around the sun at a velocity of", velocity_mars, "meters per second and has a mass of", mass_mars, "kg.")
if (speed > earth_to_mars):
    print("You are travelling fast enough to overcome the red planet. Careful not to overshoot Mars and be forever lost to the void of space.")
    print("At your current speed of", speed, "meters per second it will "
                                         "take ", time_mars, "seconds, or ", time_mars_hours, "hours to get to Mars, "
                                                                   "which is approximately", distance_mars/1000, "kilometers away!")
else:
    print("At your current speed of", speed, "you will never do battle with the god of war.")
    print("A successful rendezvous with Mars would require for the object to travel at a velocity greater than ", velocity_mars, "meters per second.")
if (speed > escape_velocity_mars):
    print("At your current rate of ", speed, " m/sec, you should have no problem escaping Mar's gravitational pull.")
else:
    print("At your current rate of ", speed, " m/sec, you will inevitably come back down to the red planet.")
if __name__ == '__main__':
    start()
