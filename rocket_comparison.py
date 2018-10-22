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
rockets = ['Saturn V', 'Atlas V', 'Delta II', 'Black Brant IV', 'Falcon 9']
thrust = [7891000, 22300, 107000, 25000, 1710000]
height = [111, 62.5, 37.8, 5.3, 70]
diameter = [10, 3.81, 2.4, 0.44, 3.7]
stages = [3, 2, 2, 2, 2]
mass = [2840622, 21173, 231870, 1265, 549054]
attributes = ['Height (h):', 'Diameter (d):', 'Thrust (t):', 'Stages (s):', 'Mass (m):']


################################
#           Saturn V           #
################################
def saturn_v():
    h = 111  # meters
    d = 10  # meters
    t = 7891000  # lbf
    s = 3  # stages
    m = 2840622  # kg
    rocket = [h, d, t, s, m]
    print(rockets[0])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")


saturn_v()


################################
#           Atlas V            #
################################
def atlas_v():
    h = 62.5  # meters
    d = 3.81  # meters
    t = 22300  # lbf
    s = 2
    m = 21173  # kg
    rocket = [h, d, t, s, m]
    print(rockets[1])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")


atlas_v()


################################
#           Detla II           #
################################
def delta_ii():
    h = 37.8  # meters
    d = 2.4  # meters
    t = 107000  # lbf
    s = 2  # or 3
    m = 231870  # kg
    rocket = [h, d, t, s, m]
    print(rockets[0])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")


delta_ii()


################################
#        Black Brant IV        #
################################
def black_brant_iv():
    h = 5.3  # meters
    d = 0.44  # meters
    t = 25000  # lbf
    s = 2
    m = 1265  # kg
    rocket = [h, d, t, s, m]
    print(rockets[0])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")


black_brant_iv()


################################
#           Falcon 9           #
################################
def falcon_9():
    h = 70  # meters
    d = 3.7  # meters
    t = 1710000  # lbf
    s = 2
    m = 549054  # kg
    rocket = [h, d, t, s, m]
    print(rockets[0])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")


falcon_9()

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

plt.show()
