# imports
import random
import sys

# Exceptions
# LocationUnavailable:

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

FARM_REQUIREMENTS = {
	'COTTON' : {'water': 10,'temperature': 10,'minerals':3},
	'TOBACCO' : {'water':3 ,'temperature':4 ,'minerals':3},
	'CHILLI' : {'water':5 ,'temperature':4 ,'minerals':4}
}

LAND_RESOURCE_LIMITS = [15, 10, 5]

FARM_RESOURCES = {
       'COTTON' : {'wood':2, 'cotton':10},
       'TOBACCO' : {'wood':3, 'tobacco':10},
       'CHILLI' : {'wood':1, 'chilli':10}
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
map_initialization_done = False
initial_forest_input = None
# Current time of the game
time = 0
# Dictionary of player's acquired resources
# Union of FARM_RESOURCES and FOREST_RESOURCE_TYPES
PLAYER_RESOURCES = {'water':50, 'wood':0, \
                    'cotton':0, 'tobacco':0, \
                    'chilli':0}
# _farm_units is a list of farm_unit objects
_farm_units = []
# _forest_units is a list of forest_unit objects
_forest_units = []
# List of possible actions the player can take
user_actions = ['Pass', 'Create Farm', 'Destroy Farm', \
	       'Harvest Farm', 'Destroy Forest', \
	       'Harvest Forest', 'List Farms', \
               'List Forests', 'List Resources', \
               'Show Map Contents']
# Index of the action selected by the player
user_input = None

