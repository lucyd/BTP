def assign_location(unit, loc):
  ''' If loc available in the map, allocates the loc location
	to unit. Else, raises LocationUnavailable exception'''
  global map_contents
  if loc in map_contents.keys():
    raise LocationUnavailable
  else:
    map_contents[loc] = unit

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
    loc.set_center(x,y)
    if loc not in map_contents.keys():
      break
  map_contents[loc] = unit
  return loc

def check_unit(loc):
  ''' If loc is allocated in the map, returns the unit allocated to.
      Else, returns None. '''
  global map_contents
  if loc in map_contents.keys():
    return map_contents[loc]
  else:
    return None

def assign_random_resources():
  ''' Returns a resources dictionary with random values  '''
  global FOREST_RESOURCE_TYPES
  global FOREST_RESOURCE_LIMITS
  resources = {}
  for i in range(len(FOREST_RESOURCE_TYPES)):
    x = random.randrange(0, FOREST_RESOURCE_LIMITS[i])
    resources[FOREST_RESOURCE_TYPES[i]] = x
  return resources

def increment_time():
  ''' Increments time by 1 '''
  global time
  time += 1

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
    new_farm_unit.change_location(unit_location(x, y))
  _farm_units.append(new_farm_unit)

def destroy_farm():
  ''' Destroys a specified farm unit '''
  global _farm_units
  print 'Enter farm-unit center coordinates:'
  x = input()
  y = input()
  for i in range(len(_farm_units)):
    if _farm_units[i].location.center == (x,y):
      _farm_units = _farm_units[:i] + _farm_units[i+1:]
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
      _farm_units = _farm_units[:i] + _farm_units[i+1:]
  print 'Farm-unit specified not found'

def destroy_forest():
  ''' Destroys a specified forest unit '''
  global _forest_units
  print 'Enter forest-unit center coordinates:'
  x = input()
  y = input()
  for i in range(len(_forest_units)):
    if _forest_units[i].location.center == (x,y):
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
      for resource in _forest_units[i].resources.keys():
        PLAYER_RESOURCES[resource] += (_forest_units[i].age * _forest_units[i].resources[resource])
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
          "  Resources:", _forest_unit.resources

def list_resources():
  ''' Lists the player's acquired resources '''
  global PLAYER_RESOURCES
  for resource in PLAYER_RESOURCES.keys():
    print resource, ": ", PLAYER_RESOURCES[resource]

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

