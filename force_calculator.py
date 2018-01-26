#
########################################################################################################################
#
####Force calculator
#
####Written By Johnathan Nicolosi
#
########################################################################################################################
#
class Rocket:
    pass
#
###############################################Saturn V - class Rocket##################################################
#
saturn_v = Rocket()
saturn_v.description = 'Saturn V rocket'
saturn_v.height = 111 # meters
saturn_v.diameter = 10 # meters
saturn_v.stages = 3 # number of stages
saturn_v.speed = 2760 # meters per second
saturn_v.T_1 = 7891000 # lbf
saturn_v.T_2 = 1155900 # lbf
saturn_v.T_3 = 225000 #lbf
saturn_v.burn_time_1 = 165 # seconds
saturn_v.burn_time_2 = 360 # seconds
saturn_v.burn_time_3 = 165 + 335 # seconds - two thrusts
saturn_v.mi_1 = 130000 #kg
saturn_v.mi_2 = 40100 #kg
saturn_v.mi_3 = 13500 #kg
saturn_v.mp_1 = 2160000 #kg
saturn_v.mp_2 = 456100 #kg
saturn_v.mp_3 = 109500 #kg
saturn_v.total_mass = saturn_v.mi_1 + saturn_v.mi_2 + saturn_v.mi_3 + saturn_v.mp_1 + saturn_v.mp_2 + saturn_v.mp_3
saturn_v.first_stage_length = 42.1 # meters
saturn_v.second_stage_length = 24.8 # meters
saturn_v.third_stage_length = 18.8 # meters
print(saturn_v.description)
print("Height:", saturn_v.height, "meters")
print("Diameter:", saturn_v.diameter, "meters")
print("Number of stages:", saturn_v.stages)
print("Travels at speeds of:", saturn_v.speed, "meters per second")
print("Total mass:", saturn_v.total_mass, "kg")
print("Total thrust, from all", saturn_v.stages, " stages, equals:", saturn_v.T_1 + saturn_v.T_2 + saturn_v.T_3, "lbf")
print("Total burn time, from all", saturn_v.stages, " stages, equals:", saturn_v.burn_time_1 + saturn_v.burn_time_2 + saturn_v.burn_time_3, "seconds")
print("")
#
#
##############################################Atlas V - class object####################################################
#
atlas_v = Rocket()
atlas_v.description = 'Atlas V rocket'
atlas_v.height = 62.5 # meters
atlas_v.diameter = 3.81 # meters
atlas_v.stages = 2 # number of stages
atlas_v.speed = 21000 # meters per second
atlas_v.T_1 = 860000 # lbf
atlas_v.T_2 = 22300 # lbf
atlas_v.burn_time_1 = 253 # seconds
atlas_v.burn_time_2 = 842 # seconds
atlas_v.mi_1 = 21054 #kg
atlas_v.mi_2 = 2316 #kg
atlas_v.mp_1 = 284089 #kg
atlas_v.mp_2 = 20830 #kg
atlas_v.total_mass = atlas_v.mi_1 + atlas_v.mi_2 + atlas_v.mp_1 + atlas_v.mp_2
atlas_v.first_stage_length = 32.46 # meters
atlas_v.second_stage_length = 12.68 # meters
print(atlas_v.description)
print("Height:", atlas_v.height, "meters")
print("Diameter:", atlas_v.diameter, "meters")
print("Number of stages:", atlas_v.stages)
print("Travels at speeds of:", atlas_v.speed, "meters per second")
print("Total mass:", atlas_v.total_mass, "kg")
print("Total thrust, from all", atlas_v.stages, " stages, equals:", atlas_v.T_1 + atlas_v.T_2, "lbf")
print("Total burn time, from all", atlas_v.stages, " stages, equals:", atlas_v.burn_time_1 + atlas_v.burn_time_2, "seconds")
print("")
#
#
#########################################Delta V - class object#########################################################
delta_ii = Rocket()
delta_ii.description = 'Delta II rocket'
delta_ii.height = 37.8 # meters
delta_ii.diameter = 2.4 # meters
delta_ii.stages = 2 # number of stages
delta_ii.speed = 9800 #meter per second
delta_ii.T_1 = 237000 # lbf
delta_ii.T_2 = 9800 # lbf
delta_ii.T_3 = 15000 # lbf
delta_ii.burn_time_1 = 265 # seconds
delta_ii.burn_time_2 = 431 # seconds
delta_ii.burn_time_3 = 87 # seconds
delta_ii.mi_1 = 26000 # kg
delta_ii.mi_2 = 3480 # kg
delta_ii.mi_3 = 0 # kg
delta_ii.mp_1 = 200400 # kg
delta_ii.mp_2 = 27220 # kg
delta_ii.mp_3 = 0 # kg
delta_ii.total_mass = delta_ii.mi_1 + delta_ii.mi_2 + delta_ii.mi_3 + delta_ii.mp_1 + delta_ii.mp_2 + delta_ii.mp_3
delta_ii.first_stage_length = 26.1 # meters
delta_ii.second_stage_length = 2.6 # meters
delta_ii.third_stage_length = 2.03 # meters
print(delta_ii.description)
print("Height:", delta_ii.height, "meters")
print("Diameter:", delta_ii.diameter, "meters")
print("Number of stages:", delta_ii.stages)
print("Travels at speeds of:", delta_ii.speed, "meters per second")
print("Total mass:", delta_ii.total_mass, "kg")
print("Total thrust, from all", delta_ii.stages, " stages, equals:", delta_ii.T_1 + delta_ii.T_2 + delta_ii.T_3, "lbf")
print("Total burn time, from all", delta_ii.stages, " stages, equals:", delta_ii.burn_time_1 + delta_ii.burn_time_2 + delta_ii.burn_time_3, "seconds")
print("")