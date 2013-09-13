# imports
import random
import sys

# Exceptions
 LocationUnavailable:

# MAP DATA
map_size = 100
# map_contents is a dict with locations as keys and 'farm' or 'forest' as values
map_contents = {
               }

# FARM DATA
FARM_UNIT_SIZE = 1
VALID_FARM_TYPES = ['COTTON', 'TOBACCO', 'CHILLI']
DEFAULT_FARM_TYPE = 'COTTON'
FARM_GROWTH_RATE = {
	        'COTTON' : 10,
		'TOBACCO' : 3,
		'CHILLI' : 5
	      }

FARM_DECAY_RATE = {
	'COTTON' : 10,
	'TOBACCO' : 3,
	'CHILLI' : 5
}

FARM_REQUIRED_RESOURCES = {
	'COTTON' : {'water': 10,'temperature': 10,'minerals':3},
	'TOBACCO' : {'water':3 ,'temperature':4 ,'minerals':3},
	'CHILLI' : {'water':5 ,'temperature':4 ,'minerals':4}
}

# FOREST DATA
FOREST_UNIT_SIZE = 1
FOREST_GROWTH_RATE = 0.5
FOREST_RESOURCE_TYPES = ['water', 'wood']
FOREST_RESOURCE_LIMITS = [100, 100]
DEFAULT_FOREST_RESOURCES = {
	"water": 20,
	"wood": 100
}

# General parameters and variables
time = 0
RESOURCES = {}
_farm_units = None
_forest_units = None
user_input = None
user_actions = ['Create Farm', 'Destroy Farm', \
	       'Harvest Farm', 'Destroy Forest', \
	       'Harvest Forest']

