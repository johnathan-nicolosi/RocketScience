# Rocket Comparison
#  Written by Johnathan Nicolosi
#
import matplotlib.pyplot as plt

################################
#           Saturn V           #
################################
saturn_h = 111 # meters
saturn_d = 10 # meters
saturn_t = 7891000 # lbf
saturn_stages = 3
saturn_mass = 2840622 #kg

################################
#           Atlas V            #
################################
atlas_h = 62.5 # meters
atlas_d = 3.81 # meters
atlas_t = 22300 # lbf
atlas_stages = 2
atlas_mass = 21173 #kg

################################
#           Detla II           #
################################
delta_h = 37.8 # meters
delta_d = 2.4 # meters
delta_t = 107000 # lbf
delta_stages = 2 # or 3
delta_mass = 231870 # kg

################################
#        Black Brant IV        #
################################
brant_h = 5.3 # meters
brant_d = 0.44 # meters
brant_t = 25000 # lbf
brant_stages = 2
brant_mass = 1265 # kg

################################
#           Falcon 9           #
################################
falcon_h = 70 # meters
falcon_d = 3.7 # meters
falcon_t = 1710000 # lbf
falcon_stages = 2
falcon_mass = 549054 # kg

################################
#       Rocket Comparison      #
################################
rockets = ['Saturn V', 'Atlas V', 'Delta II', 'Black Brant IV', 'Falcon 9']
thrust = [7891000, 22300, 107000, 25000, 1710000]
height = [111, 62.5, 37.8, 5.3, 70]
diameter = [10, 3.81, 2.4, 0.44, 3.7]
stages = [3, 2, 2, 2, 2]
mass = [2840622, 21173, 231870, 1265, 549054]


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
#plt.bar(rockets, stages)

plt.subplot(212)
plt.bar(rockets, thrust)
plt.ylabel('Thrust (lbf)')

plt.show()