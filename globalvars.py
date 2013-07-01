# imports
import random
import sys

# Exceptions
 LocationUnavailable:

time = 0

# MAP DATA
map_size = 100
# map_contents is a dict with locations as keys and 'farm' or 'forest' as values
map_contents = {
                unit_location(): 'farm'
               }

# FARM DATA
FARM_UNIT_SIZE = 1
VALID_FARM_TYPES = ['COTTON', 'TOBACCO', 'CHILLI']
DEFAULT_FARM_TYPE = 'COTTON'
GROWTH_RATE = {
	        'COTTON' : 10,
		'TOBACCO' : 3,
		'CHILLI' : 5
	      }

DECAY_RATE = {
	'COTTON' : 10,
	'TOBACCO' : 3,
	'CHILLI' : 5
}

REPRODUCTION_RATE = {
	'COTTON' : 10,
	'TOBACCO' : 3,
	'CHILLI' : 5
}

REQUIRED_RESOURCES = {
	'COTTON' : {'water': 10,'temperature': 10,'minerals':3},
	'TOBACCO' : {'water':3 ,'temperature':4 ,'minerals':3},
	'CHILLI' : {'water':5 ,'temperature':4 ,'minerals':4}
}

# FOREST DATA
FOREST_UNIT_SIZE = 1
DEFAULT_FOREST_RESOURCES = {
	"water": 20,
	"wood": 100
}


