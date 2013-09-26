# Game: farm-forest

# Global Variables
# imports
import random
import sys

# Exceptions
# LocationUnavailable:

# MAP DATA
map_size = 100
map_initialization_done = False
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
FARM_RESOURCE_TYPES = ['cotton', 'tobacco', 'chilli']
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
initial_forest_input = None
# Current time of the game
time = 0
score = 0
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



# Object Definitions
class unit_location:
  ''' A location of an unit'''
  def __init__(self, x=None, y=None):
    self.center = (x, y)
    self.resources = assign_random_resources('land')

  def set_resources(self, _resources):
    self.resources = _resources

  def set_center(self, x, y):
    self.center = (x, y)

  def get_center(self):
    return self.center

class farm_unit:
  ''' The farm unit class '''
  def __init__(self, _type=None):
    if _type == None or _type.strip() == '' \
	      or _type not in VALID_FARM_TYPES:
      self.farm_type = DEFAULT_FARM_TYPE
    else:
      self.farm_type = _type
    self.location = assign_random_location("farm")
    self.age = 0
    
  def change_location(self, loc):
    self.location = loc

  def get_location(self):
    return self.location

  def change_type(self, _type):
    # _type is a valid farm unit type
    self.farm_type = _type

  def get_type(self):
    return self.farm_type

class forest_unit:
  ''' The forest unit class '''
  def __init__(self):
    self.location = assign_random_location("forest")
    self.location.set_resources(assign_random_resources("forest"))
    self.age = 0

  def change_location(self, loc):
    self.location = loc

  def get_location(self):
    return self.location


# Methods
def assign_random_location(unit):
  ''' Selects a random location from the map and assigns it as the unit '''
  global FARM_UNIT_SIZE
  global FOREST_UNIT_SIZE
  global map_size
  global map_contents
  size = 1
  if unit == 'farm':
    size = FARM_UNIT_SIZE
  elif unit == 'forest':
    size = FOREST_UNIT_SIZE
  loc = unit_location()
  while True:
    x = random.randrange(0+size, map_size-size)
    y = random.randrange(0+size, map_size-size)
    if check_map(x,y) is None:
      break
  loc.set_center(x,y)
  map_contents[loc] = unit
  return loc

def check_map(x, y):
  ''' If (x,y) is allocated in the map, returns the unit allocated to.
      Else, returns None. '''
  global map_contents
  for loc in map_contents.keys():
    if loc.center == (x,y):
      return map_contents[loc]
  return None

def farm_requirements_satisifed(x, y, farm_type):
  ''' Returns 1 if location satisfied farm's requirements,
      0 otherwise '''
  global FARM_REQUIREMENTS
  loc_resources = get_resources(x, y)
  required_resources = FARM_REQUIREMENTS[farm_type]
  for resource in required_resources:
    if resource not in loc_resources.keys() or required_resources[resource] > loc_resources[resource]:
      return 0
  return 1

def delete_location(x, y):
  ''' Removes the location from map_contents '''
  for loc in map_contents.keys():
    if loc.center == (x,y):
      map_contents.pop(loc, None)

def assign_random_resources(_type):
  ''' Returns a resources dictionary with random values  '''
  global FOREST_RESOURCE_TYPES
  global FOREST_RESOURCE_LIMITS
  global FARM_REQUIREMENTS
  global LAND_RESOURCE_LIMITS
  resources = {}
  if _type == 'forest':
    resource_types = FOREST_RESOURCE_TYPES
    resource_limits = FOREST_RESOURCE_LIMITS
  elif _type == 'land':
    resource_types = FARM_REQUIREMENTS.keys()
    resource_limits = LAND_RESOURCE_LIMITS
  for i in range(len(resource_types)):
    x = random.randrange(0, resource_limits[i])
    resources[resource_types[i]] = x
  return resources

def get_resources(x, y):
  ''' Returns the resources dict of the location '''
  global map_contents
  for loc in map_contents.keys():
    if loc.center == (x,y):
      return loc.resources
  return {}

def increment_time():
  ''' Increments time by 1 '''
  global time
  time += 1

def initialize_map():
  ''' Initializes map with locations '''
  global map_contents
  global map_size
  global map_initialization_done
  for i in range(map_size):
    for j in range(map_size):
      if random.randrange(2) == 0:
        loc = unit_location()
        loc.set_center(i,j)
        map_contents[loc] = 'land'
  map_initialization_done = True

def update_score():
  ''' Updates the score '''
  global score
  global time
  global PLAYER_RESOURCES
  global _forest_units
  global _farm_units
  global FOREST_RESOURCE_TYPES
  global FARM_RESOURCE_TYPES
  score = len(_forest_units) + len(_farm_units)
  for resource in FOREST_RESOURCE_TYPES + FARM_RESOURCE_TYPES:
    score += PLAYER_RESOURCES[resource]
  score -= time
  score -= 49

def simulate_farm_growth():
  ''' Simulates the farm growth '''
  global _farm_units
  global FARM_GROWTH_RATE
  for _farm_unit in _farm_units:
    _farm_unit.age += (FARM_GROWTH_RATE[_farm_unit.farm_type])

def simulate_forest_growth():
  ''' Simulates the forest growth '''
  global _forest_units
  global FOREST_GROWTH_RATE
  for _forest_unit in _forest_units:
    _forest_unit.age += FOREST_GROWTH_RATE

def create_farm():
  ''' Creates a custom farm unit '''
  global VALID_FARM_TYPES
  global _farm_units
  new_farm_unit = farm_unit()
  print 'Select farm type'
  for i in range(len(VALID_FARM_TYPES)):
    print i, ': ', VALID_FARM_TYPES[i]
  farm_type = input()
  new_farm_unit.change_type(VALID_FARM_TYPES[farm_type]) 
  is_location_random = ''
  while is_location_random not in ['Y', 'N']:
    print 'Randomize location? (Y/N) : ',
    is_location_random = raw_input()
  if is_location_random == 'N':
    print 'Enter farm-unit center co-ordinates: '
    x = input()
    y = input()
    if check_map(x,y) is None and \
      farm_requirements_satisfied(x,y,VALID_FARM_TYPES[farm_type]):
        new_loc = unit_location(x,y)
        new_farm_unit.change_location(new_loc)
        map_contents[new_loc] = 'farm'
    else:
      print 'Oops!!! Location already assigned'
      return
  _farm_units.append(new_farm_unit)

def destroy_farm():
  ''' Destroys a specified farm unit '''
  global _farm_units
  print 'Enter farm-unit center coordinates:'
  x = input()
  y = input()
  for i in range(len(_farm_units)):
    if _farm_units[i].location.center == (x,y):
      delete_location(x,y)
      _farm_units = _farm_units[:i] + _farm_units[i+1:]
      return
  print 'Farm-unit specified not found'

def harvest_farm():
  ''' Remove and harvest a farm unit's resources '''
  global _farm_units
  global FARM_RESOURCES
  global PLAYER_RESOURCES
  print 'Enter farm-unit center coordinates:'
  x = input()
  y = input()
  for i in range(len(_farm_units)):
    if _farm_units[i].location.center == (x,y):
      _farm_resources = FARM_RESOURCES[_farm_units[i].farm_type]
      for resource in _farm_resources.keys():
        PLAYER_RESOURCES[resource] += (_farm_units[i].age * _farm_resources[resource])
      delete_location(x,y)
      _farm_units = _farm_units[:i] + _farm_units[i+1:]
      return
  print 'Farm-unit specified not found'

def destroy_forest():
  ''' Destroys a specified forest unit '''
  global _forest_units
  print 'Enter forest-unit center coordinates:'
  x = input()
  y = input()
  for i in range(len(_forest_units)):
    if _forest_units[i].location.center == (x,y):
      delete_location(x,y)
      _forest_units = _forest_units[:i] + _forest_units[i+1:]
      return
  print 'Forest-unit specified not found'

def harvest_forest():
  ''' Kill and harvest a forest unit's resources '''
  global _forest_units
  global PLAYER_RESOURCES
  print 'Enter forest-unit center coordinates:'
  x = input()
  y = input()
  for i in range(len(_forest_units)):
    if _forest_units[i].location.center == (x,y):
      for resource in _forest_units[i].location.resources.keys():
        PLAYER_RESOURCES[resource] += (_forest_units[i].age * _forest_units[i].location.resources[resource])
      delete_location(x,y)
      _forest_units = _forest_units[:i] + _forest_units[i+1:]
      return
  print 'Forest-unit specified not found'

def list_farms():
  ''' Lists all the farm units '''
  global _farm_units
  if _farm_units == []:
    print 'No farm units in the map'
    return
  for _farm_unit in _farm_units:
    print "Type:", _farm_unit.farm_type, \
          "  Center:", _farm_unit.location.center, \
          "  Age:", _farm_unit.age

def list_forests():
  ''' Lists all the forest units '''
  global _forest_units
  if _forest_units == []:
    print 'No forest units in the map'
    return
  for _forest_unit in _forest_units:
    print "Center:", _forest_unit.location.center, \
          "  Age:", _forest_unit.age, \
          "  Resources:", _forest_unit.location.resources

def list_resources():
  ''' Lists the player's acquired resources '''
  global PLAYER_RESOURCES
  for resource in PLAYER_RESOURCES.keys():
    print resource, ": ", PLAYER_RESOURCES[resource]

def show_map_contents():
  ''' Displays the map contents '''
  global map_size
  for i in range(map_size):
    for j in range(map_size):
      print 'Co-ordinates: ', (i,j),
      print 'Resources: ', get_resources(i,j)

def game_over():
  ''' Called when constraints for finishing of game are satisfied '''
  global score
  print '\n----Game over----\n'
  print 'Thank you for playing the game'
  print 'Your final score: ', score, '\n'
  sys.exit(1)

def get_initial_forest_input():
  ''' Initializes the forests in the map '''
  global _forest_units
  global initial_forest_input
  _forest_units = []
  print 'Enter initial no.of forests: '
  total_forests = input()
  for i in range(total_forests):
    _forest_units.append(forest_unit())
  initial_forest_input = total_forests

def get_user_input():
  ''' Receives the user input '''
  global user_actions
  print 'Select one of the following actions'
  for i in range(len(user_actions)):
    print i, ": ", user_actions[i]
  user_input = input()
  return user_input

def process_user_input(user_input):
  ''' Takes appropriate action based on user input '''
  global user_actions
  user_action = user_actions[user_input] 
  if user_action == 'Pass':
    return
  elif user_action == 'Create Farm':
    create_farm()
  elif user_action == 'Destroy Farm':
    destroy_farm()
  elif user_action == 'Harvest Farm':
    harvest_farm()
  elif user_action == 'Destroy Forest':
    destroy_forest()
  elif user_action == 'Harvest Forest':
    harvest_forest()
  elif user_action == 'List Farms':
    list_farms()
  elif user_action == 'List Forests':
    list_forests()
  elif user_action == 'List Resources':
    list_resources()
  elif user_action == 'Show Map Contents':
    show_map_contents()



# Infinite game loop
while True:
  if map_initialization_done == False :
     initialize_map()
  if True :
     increment_time()
  if initial_forest_input == None :
     get_initial_forest_input()
  if True :
     update_score()
  if len(_forest_units) == 0 :
     game_over()
  if True :
     simulate_farm_growth()
  if True :
     simulate_forest_growth()
  if True :
     process_user_input(get_user_input())
