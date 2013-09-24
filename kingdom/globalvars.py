# imports
import random
import sys

# Exceptions
# LocationUnavailable:

# MAP DATA
map_size = 100
# map_contents is a dict with locations as keys and 'farm' or 'forest' as values
map_contents = {}

# FARM DATA
FARM_UNIT_SIZE = 1
VALID_FARM_TYPES = ['COTTON', 'TOBACCO', 'CHILLI']
DEFAULT_FARM_TYPE = 'COTTON'
# FARM_GROWTH_RATE values could be exponentially decreasing functions
FARM_GROWTH_RATE = {
	        'COTTON' : 10,
		'TOBACCO' : 3,
		'CHILLI' : 5
}

FARM_LIFE_SPAN = {
	'COTTON': 100,
	'TOBACCO': 130,
	'CHILLI': 70
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
VALID_INDUSTRY_TYPES = ['TOBACCO', 'CLOTHING']
DEFAULT_INDUSTRY_TYPE = ['CLOTHING']
PRODUCTION_RATE = {
	           'TOBACCO': 10,
		   'CLOTHING': 25
		  }
# HOSPITAL DATA
HOSPITAL_UNIT_SIZE = 1
TREATMENT_COST = 10

SCHOOL_UNIT_SIZE = 1
UNIVERSITY_UNIT_SIZE = 1

# General parameters and variables
# Current time of the game
time = 0
# Value of one year
year = 50
# Player score
SCORE = {'Agriculture': 0, 'Industry':0, 'Health/Safety':0, \
         'Finance':0, 'Trade':0, 'Culture':0, 'Education':0, \
         'Residence':0}
# Kingdom population
population = 0
# Employed population
employed_population = 0
# Workers needed for full employment
workers_needed = 0
# Employees required for each of the units
EMPLOYEES_REQUIRED = {'Farm': 5, 'Industry': 10, 'School': 10, \
                      'University': 10, 'Hospital': 5, 'Tax Office':5, \
                      'Trade Office':5, 'Construction': 10}
# Tax value
tax = 0
# Wages value
wages = 0
# Budget value
budget = 0
# Allocated budget values
ALLOCATED_BUDGET = {'Agriculture':0, 'Industry':0, 'Health/Safety':0, \
                    'Finance':0, 'Trade':0, 'Culture':0, 'Education':0, \
                    'Residence':0}
# Cost of building various units
COST = {'Farm': 5, 'Industry': 10, 'Hospital': 10, 'School': 5, \
        'University': 10, 'House': 5, 'Festival': 50}
# Dictionary of player's acquired resources(raw materials and products)
PLAYER_RESOURCES = {'water':0, 'wood':0, 'cotton':0, 'tobacco':0, \
                    'chilli':0, 'cigarette':0}
# farms is a list of farm objects
farms = []
# industries is a list of industry objects
industries = []
# hospitals is a list of hospital objects
hospitals = []
# schools is a list of school objects
schools = []
# universities is a list of university objects
universities = []
# List of possible actions the player can take
agriculture_actions = ['Create farms', 'Destroy farms']
industry_actions = ['Create industries', 'Destroy industries', \
		    'Change production rate']
health_actions = ['Create hospital/infirmary', 'Destroy hospital/infirmary', \
		  'Change treatment/medicine cost']
finance_actions = ['Change tax', 'Change wages', 'Change budget allocation']
trade_actions = ['Create new trade route', 'Remove existing trade route', \
		 'Change export price', 'Change import policy', 'Change export policy']
culture_actions = ['Arrage festival', 'Build cultural unit']
education_actions = ['Build school', 'Build university', \
		     'Destroy school', 'Destroy university']
residence_actions = ['Build houses', 'Destroy houses']
general_actions = ['List farms', 'List industries', 'List hospitals/infirmaries', \
                   'List schools', 'List universities', 'List houses', \
                   'Check population', 'Check production rates', 'Check treatment cost', \
                   'Check tax', 'Check wages', 'Check budget allocation']
# Possible domains in which actions can be taken
DOMAINS = {'Agriculture': agriculture_actions, 'Industry': industry_actions, \
	   'Health/Safety': health_actions, 'Finance': finance_actions, \
	   'Trade': trade_actions, 'Culture': culture_actions, \
	   'Education': education_actions, 'Residence': residence_actions, \
           'General': general_actions}

# TRADE DATA
trade_routes = ['India', 'America', 'China']
# Import price data for available trade routes
AVAILABLE_IMPORTS = {'chilli': {'India':5}, \
                     'cotton': {'India':5}, \
                     'cigarette': {'America':10}, \
                     'wood': {'China': 5}}
# Export price data for available trade routes
AVAILABLE_EXPORTS = {'cigarette': {'India': 10}, \
                     'chilli': {'America': 5}, \
                     'cotton': {'China': 5}}
# List of kingdoms importing from
established_trade_routes = []
# List of 3-tuples of kingdoms, type of goods importing and number
import_goods = []
# List of 3-tuples of kingdoms, type of goods exporting and number
export_goods = []
