########################################################
#                                                      #
#                  Rocket Comparison                   #
#            Written by Johnathan Nicolosi             #
#                                                      #
########################################################

import matplotlib.pyplot as plt


################################
#       Rocket Comparison      #
################################
rockets = ['Ariane 5', 'Atlas V', 'Black Brant IV', 'Delta II', 'Delta IV', 'Falcon 9', 'Saturn V']
height = [46, 58.3, 11.06, 37.8, 63, 70, 110.6] # meters
diameter = [5.4, 3.81, 0.44, 2.4, 5, 3.7, 10] # meters
thrust = [220000, 860000, 24953, 237000, 705000, 1710000, 7891000] # lbf
mass = [777000, 334500, 1356, 151700, 249500, 549054, 2840622] # kg
stages = [2, 2, 2, 2, 2, 2, 3]
attributes = ['Height (h):', 'Diameter (d):', 'Thrust (t):', 'Mass (m):', 'Stages (s):']


################################
#           Ariane 5           #
################################
def ariane_5():
    print(rockets[0])
    print(attributes[0], height[0], "(m)")
    print(attributes[1], diameter[0], "(m)")
    print(attributes[2], thrust[0], "(lbf)")
    print(attributes[3], mass[0], "(kg)")
    print(attributes[4], stages[0])
    print("")
ariane_5()

################################
#           Atlas V            #
################################
def atlas_v():
    print(rockets[1])
    print(attributes[0], height[1], "(m)")
    print(attributes[1], diameter[1], "(m)")
    print(attributes[2], thrust[1], "(lbf)")
    print(attributes[3], mass[1], "(kg)")
    print(attributes[4], stages[1])
    print("")
atlas_v()

################################
#        Black Brant IV        #
################################
def black_brant_iv():
    print(rockets[2])
    print(attributes[0], height[2], "(m)")
    print(attributes[1], diameter[2], "(m)")
    print(attributes[2], thrust[2], "(lbf)")
    print(attributes[3], mass[2], "(kg)")
    print(attributes[4], stages[2])
    print("")
black_brant_iv()

################################
#           Detla II           #
################################
def delta_ii():
    print(rockets[3])
    print(attributes[0], height[3], "(m)")
    print(attributes[1], diameter[3], "(m)")
    print(attributes[2], thrust[3], "(lbf)")
    print(attributes[3], mass[3], "(kg)")
    print(attributes[4], stages[3])
    print("")
delta_ii()

################################
#           Detla IV           #
################################
def delta_iv():
    print(rockets[4])
    print(attributes[0], height[4], "(m)")
    print(attributes[1], diameter[4], "(m)")
    print(attributes[2], thrust[4], "(lbf)")
    print(attributes[3], mass[4], "(kg)")
    print(attributes[4], stages[4])
    print("")
delta_iv()

################################
#           Falcon 9           #
################################
def falcon_9():
    print(rockets[5])
    print(attributes[0], height[5], "(m)")
    print(attributes[1], diameter[5], "(m)")
    print(attributes[2], thrust[5], "(lbf)")
    print(attributes[3], mass[5], "(kg)")
    print(attributes[4], stages[5])
    print("")
falcon_9()

################################
#           Saturn V           #
################################
def saturn_v():
    print(rockets[6])
    print(attributes[0], height[6], "(m)")
    print(attributes[1], diameter[6], "(m)")
    print(attributes[2], thrust[6], "(lbf)")
    print(attributes[3], mass[6], "(kg)")
    print(attributes[4], stages[6])
    print("")
saturn_v()


#################################
# Plotting Figures (Matplotlib) #
#################################
plt.title('Rocket Comparison')
plt.figure(1)
plt.subplot(211)
plt.title('Diameter Vs Height')
plt.bar(rockets, diameter)
plt.ylabel('Diameter (meters)')

plt.subplot(212)
plt.bar(rockets, height)
plt.ylabel('Height (meters)')

plt.figure(2)
plt.subplot(211)
plt.title('Mass Vs Thrust')
plt.bar(rockets, mass)
plt.ylabel('Mass (kg)')

plt.subplot(212)
plt.bar(rockets, thrust)
plt.ylabel('Thrust (lbf)')

# This section turns off scientific notation
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_scientific(False)

plt.show()
