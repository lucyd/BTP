def assign_location(unit, loc):
  ''' If loc available in the map, allocates the loc location
	to unit. Else, raises LocationUnavailable exception'''
  if loc in map_contents.keys():
    raise LocationUnavailable
  else:
    map_contents[loc] = unit

def assign_random_location(unit):
  ''' Selects a random location from the map and assigns it as the unit '''
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
  if loc in map_contents.keys():
    return map_contents[loc]
  else:
    return None

def assign_random_resources():
  resources = {}
  for i in range(len(RESOURCE_TYPES)):
    resources[RESOURCE_TYPES[i]] = random.randrange(0,RESOURCE_LIMITS[i])
  return resources

def increment_time():
  ''' Increments time by 1 '''
  time += 1

def farm_growth(loc):
  ''' Simulates the farm growth '''
  for _farm_unit in _farm_units:
    _farm_unit.age += 1

def forest_growth():
  ''' Simulates the forest growth '''
  for _forest_unit in _forest_units:
    _forest_unit.age += 1

def create_farm():
  ''' Creates a custom farm unit '''
  new_farm_unit = farm_unit()
  print 'Select farm type'
  for i in range(VALID_FARM_TYPES):
    print i, ': ', VALID_FARM_TYPES[i]
  farm_type = input()
  new_farm_unit.change_type(VALID_FARM_TYPES[farm_type]) 
  print 'Randomize location? (Y/N) : '
  is_location_random = 'Y'
  while is_location_random not in ['Y', 'N']:
    is_location_random = raw_input()
  if is_location_random == 'N':
    print 'Enter farm-unit center co-ordinates: '
    x = input()
    y = input()
    new_farm_unit.change_location(unit_location(x, y))
  _farm_units.append(new_farm_unit)

def destroy_farm():
  ''' Destroys a specified farm unit '''

def harvest_farm():
  ''' Kill and harvest a farm unit's resources '''

def destroy_forest():
  ''' Destroys a specified forest unit '''

def harvest_forest():
  ''' Kill and harvest a forest unit's resources '''

def get_farm_input():
  ''' Initializes the farms in the map '''
  print 'Enter no.of farms: '
  total_farms = input()
  for i in range(total_farms):
    print 'Farm ',i+1, '- Enter farm type: '
    _farm_units[i] = farm_unit(raw_input())

def get_forest_input():
  ''' Initializes the forests in the map '''
  print 'Enter no.of forests: '
  total_forests = input()
  for i in range(total_forests):
    _forest_units[i] = forest_unit()

def get_user_input():
  ''' Receives the unchecked user input '''
  print 'Select one of the following actions'
  for i in range(len(user_actions)):
    print i, ": ", user_actions[i]
  user_input = input()
  return user_input

def process_user_input(user_input):
  ''' Takes appropriate action based on user input '''
  user_action = user_actions[user_input] 
  if user_action == 'Create Farm':
    create_farm()
  elif user_action == 'Destroy Farm':
    destroy_farm()
  elif user_action == 'Harvest Farm':
    harvest_farm()
  elif user_action == 'Destroy Forest':
    destroy_forest()
  elif user_action == 'Harvest Forest':
    harvest_forest()

