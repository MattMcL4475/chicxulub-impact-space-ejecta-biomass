import math

asteroid_diameter = 14 # km
asteroid_density = 3000 # in kg/m3  (typical rocky asteroid)
ejecta_ratio = 0.1 # fraction of asteroid volume that becomes ejecta
space_ratio = 0.01 # fraction of ejecta that reaches space
bacteria_per_m3 = 1e12 # could be up to 1e14
asteroid_radius_in_m = (asteroid_diameter / 2) * 1000
asteroid_volume = (4/3) * math.pi * (asteroid_radius_in_m ** 3)
ejecta_volume = asteroid_volume * ejecta_ratio
space_volume = ejecta_volume * space_ratio # volume of ejecta that reached space
bacteria_ejected_to_space = space_volume * bacteria_per_m3
bacteria_ejected_to_space_in_trillions = bacteria_ejected_to_space / 1e12
bacteria_that_survived_ejection_ratio = .1
bacteria_that_can_survive_in_space_ratio = .00001 # d. radiodurans, t. gammatolerans, b. subtilis, e. coli,  chroococcidiopsis (tardigrades omitted!)
bacteria_ejected_to_space_alive = bacteria_ejected_to_space * bacteria_that_survived_ejection_ratio * bacteria_that_can_survive_in_space_ratio
probability_bacteria_landed_on_mars = 0.000001
bacteria_that_landed_on_mars = bacteria_ejected_to_space_alive * probability_bacteria_landed_on_mars

print(f"Estimated # of bacteria that landed on Mars from the Chicxulub impact: {bacteria_that_landed_on_mars:.2f}")
# Estimated # of bacteria that landed on Mars from the Chicxulub impact: 1436755040.24
