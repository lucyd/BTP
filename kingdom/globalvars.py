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
# FARM_GROWTH_RATE values could possibly be exponentially decreasing functions
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

FARM_RESOURCES = {
       'COTTON' : {'wood':2, 'cotton':10},
       'TOBACCO' : {'wood':3, 'tobacco':10},
       'CHILLI' : {'wood':1, 'chilli':10}
}

# INDUSTRY DATA
INDUSTRY_UNIT_SIZE = 1
INDUSTRY_TYPES = ['TOBACCO', 'CLOTHING']
DEFAULT_INDUSTRY_TYPE = ['CLOTHING']
PRODUCTION_RATE = {
	           'TOBACCO': 10
		   'CLOTHING': 25
		  }

# General parameters and variables
# Current time of the game
time = 0
# Player score
score = {'Agriculture': 0, 'Industry':0, 'Health/Safety':0, \
         'Finance':0, 'Trade':0, 'Culture':0, 'Education':0, \
         'Residence':0}
# Kingdom population
population = 0
# Dictionary of player's acquired resources(raw materials and products)
PLAYER_RESOURCES = {'water':0, 'wood':0, 'cotton':0, 'tobacco':0, \
                    'chilli':0, 'cigarette'}
# farms is a list of farm objects
farms = []
# industries is a list of industry objects
industries = []
# List of possible actions the player can take
agriculture_actions = ['Create farms', 'Destroy farms', 'List farms']
industry_actions = ['Create industries', 'Destroy industries', \
		    'List industries', 'Limit production rate']
health_actions = ['Create hospital/infirmary', 'Destroy hospital/infirmary', \
		  'List hospitals/infirmaries', 'Modify treatment/medicine price']
finance_actions = ['Modify tax', 'Modify wages', 'Modify budget allocation']
trade_actions = ['Create new trade route', 'Destroy existing trade route', \
		 'Modify export price', 'Modify import policy', 'Modify export policy']
culture_actions = ['Arrage a festival', 'Build a cultural unit']
education_actions = ['Build school', 'Build university', \
		     'Destroy school', 'Destroy university']
residence_actions = ['Build houses', 'Destroy houses']
# Index of the action selected by the player
user_input = None

