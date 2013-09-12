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
  for resource in RESOURCE_TYPES:
    resources[resource] = random.randrange(0,100)
  return resources

def increment_farm_age(loc):
  ''' Increments the age of every farm unit by 1 '''
  for _farm_unit in _farm_units:
    _farm_unit.age += 1

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
  user_input = raw_input()

def increment_time():
  ''' Increments time by 1 '''
  time += 1

#def process_user_input()
#  ''' Takes appropriate action based on user input '''
   
