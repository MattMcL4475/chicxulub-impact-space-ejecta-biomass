# Copyright (c) Matthew H. McLoughlin.
# Licensed under the MIT License.

import math

asteroid_diameter = 14 # km
asteroid_density = 3000 # in kg/m3  (typical rocky asteroid)
ejecta_ratio = 0.1 # fraction of asteroid volume that becomes ejecta
space_ratio = 0.01 # fraction of ejecta that reaches space
bacteria_per_m3 = 1e12 # could be up to 1e14
bacteria_that_survived_ejection_ratio = .1
bacteria_that_can_survive_in_space_ratio = .00001 # d. radiodurans, t. gammatolerans, b. subtilis, e. coli,  chroococcidiopsis (tardigrades omitted!)
bacteria_that_survived_space_journey_ratio = 0.1
probability_bacteria_landed_on_a_habitable_planet_or_moon = 0.000001

asteroid_radius_in_m = (asteroid_diameter / 2) * 1000
asteroid_volume = (4/3) * math.pi * (asteroid_radius_in_m ** 3)
ejecta_volume = asteroid_volume * ejecta_ratio
space_volume = ejecta_volume * space_ratio # volume of ejecta that reached space
bacteria_ejected_to_space = space_volume * bacteria_per_m3
bacteria_ejected_to_space_alive = bacteria_ejected_to_space * bacteria_that_survived_ejection_ratio * bacteria_that_can_survive_in_space_ratio
bacteria_that_landed_on_a_habitable_planet_or_moon = bacteria_ejected_to_space_alive * probability_bacteria_landed_on_a_habitable_planet_or_moon

print(f"Estimated # of bacteria that landed alive on a habitable planet or moon from the Chicxulub impact: {bacteria_that_landed_on_a_habitable_planet_or_moon:.2f}")

# Result
# Estimated # of bacteria that landed alive on a habitable planet or moon from the Chicxulub impact: 1436755040.24
