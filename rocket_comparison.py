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
    h = 46  # meters
    d = 5.4  # meters
    t = 220000  # lbf
    m = 777000  # kg
    s = 2  # stages
    rocket = [h, d, t, m, s]
    print(rockets[0])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")
ariane_5()

################################
#           Atlas V            #
################################
def atlas_v():
    h = 58.3  # meters
    d = 3.81  # meters
    t = 860000  # lbf
    m = 334500  # kg
    s = 2
    rocket = [h, d, t, m, s]
    print(rockets[1])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")
atlas_v()

################################
#        Black Brant IV        #
################################
def black_brant_iv():
    h = 11.06  # meters
    d = 0.44  # meters
    t = 24953  # lbf
    m = 1356  # kg
    s = 2
    rocket = [h, d, t, m, s]
    print(rockets[0])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")
black_brant_iv()

################################
#           Detla II           #
################################
def delta_ii():
    h = 37.8  # meters
    d = 2.4  # meters
    t = 237000  # lbf
    m = 151700  # kg
    s = 2  # or 3
    rocket = [h, d, t, m, s]
    print(rockets[0])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")
delta_ii()

################################
#           Detla IV           #
################################
def delta_iv():
    h = 63  # meters
    d = 5  # meters
    t = 705000  # lbf
    m = 249500  # kg
    s = 2
    rocket = [h, d, t, m, s]
    print(rockets[0])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")
delta_iv()

################################
#           Falcon 9           #
################################
def falcon_9():
    h = 70  # meters
    d = 3.7  # meters
    t = 1710000  # lbf
    m = 549054  # kg
    s = 2
    rocket = [h, d, t, m, s]
    print(rockets[0])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
    print("")
falcon_9()

################################
#           Saturn V           #
################################
def saturn_v():
    h = 110.6  # meters
    d = 10  # meters
    t = 7891000  # lbf
    m = 2840622  # kg
    s = 3  # stages
    rocket = [h, d, t, m, s]
    print(rockets[0])
    print(attributes[0], rocket[0])
    print(attributes[1], rocket[1])
    print(attributes[2], rocket[2])
    print(attributes[3], rocket[3])
    print(attributes[4], rocket[4])
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

plt.figure(3)
plt.subplot(311)
plt.title('Height Vs Stages')
plt.bar(rockets, height)
plt.ylabel('Height (m)')

plt.subplot(312)
plt.bar(rockets, stages)
plt.ylabel('Stages')

plt.show()
