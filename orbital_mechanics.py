###############################
#Orbital Mechanics 101        #
#                             #
#Written by Johnathan Nicolosi#
#                             #
###############################

print("The amount of force behind an object equals the mass of the object and its rate of acceleration.\n"
      "Therefore, massive objects moving at greater speeds have more force behind them than do smaller,\n"
      "slower-moving objects.")
mass=int(input("Enter the mass of an object in kilograms: "))
speed=float(input("Enter speed of object in meters per second: "))
time=1
acceleration = speed / time
force= mass * acceleration
#
mass_earth=5.972*10**24 #kg
velocity_earth=30000
gravity_earth=9.8
weight_earth=mass * gravity_earth #kg
escape_velocity=11200
escape_force_earth=mass * escape_velocity
#
mass_moon=7.34767309*10**22 #kg
velocity_moon=1000
gravity_moon=1.622
weight_moon=mass * gravity_moon
distance_moon=384472282
relative_speed_moon=speed-velocity_moon
escape_velocity_moon=2380
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
#
mass_ceres=9.39*10**20 #kg
escape_velocity_ceres=510
#
print("The weight of the object is", weight_earth, "lbs")
print("The force behind that object is", force, "Newtons")
print("")
print("With this knowledge, we can calculate the amount of force required for an object to break free of "
      "Earth's gravity.")
print("In order to escape Earth's gravity, an object must travel at approximately", escape_velocity, "km/s.")
print("Travelling at", escape_velocity, "meters per second, the force "
                                              "behind the object will be", escape_force_earth, "Newtons.")
print("")
print("At your current speed of", speed, "meters per second "
                                         "it will take ", time_moon_hours, "hours to get to the moon, "
                                        "which is approximately", distance_moon, "meters away!")
print("")
print("The moon is travelling around the earth at a rate of", velocity_moon, "meters per second.")
print("Therefore, for every hour of spaceflight, the moon will travel", velocity_moon*3600, "meters.")
print("At your current speed "
      "of", speed, "it will take an additional", time_moon, "seconds, or", time_moon / 3600, "hours to catch the moon.")
print("")
print("Mars is travelling around the sun at a rate of", velocity_mars, "meters per second.")
print("For every hour of spaceflight, Mars will have travelled", velocity_mars*3600, "meters.")
print("At your current speed "
      "of", speed, "it will take an additional", time_mars, "seconds, "
                                                            "or", time_mars / 3600, "hours to catch the red planet.")
print("")



