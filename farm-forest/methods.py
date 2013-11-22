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
    update_training_data(user_input)
  elif user_action == 'Destroy Farm':
    destroy_farm()
    update_training_data(user_input)
  elif user_action == 'Harvest Farm':
    harvest_farm()
    update_training_data(user_input)
  elif user_action == 'Destroy Forest':
    destroy_forest()
    update_training_data(user_input)
  elif user_action == 'Harvest Forest':
    harvest_forest()
    update_training_data(user_input)
  elif user_action == 'List Farms':
    list_farms()
  elif user_action == 'List Forests':
    list_forests()
  elif user_action == 'List Resources':
    list_resources()
  elif user_action == 'Show Map Contents':
    show_map_contents()

def update_training_data(last_action):
  ''' Updates the training data with the current parameters
      Argument passed is the latest action taken by the user '''
  global training_data
  global _farm_units
  global _forest_units
  global PLAYER_RESOURCES
  training_sample = []
  training_sample.append(len(_farm_units))
  training_sample.append(len(_forest_units))
  for _resource in PLAYER_RESOURCES.values():
    training_sample.append(_resource)
  training_sample.append(last_action)
  training_data.append(training_sample)

def zero_index():
  ''' Trigger event for decision of index 0 '''
  return

def one_index():
  ''' Trigger event for decision of index 1 
      Decrease resource-limit of a random farm type '''
  global FARM_RESOURCES
  farm_resources_keys = FARM_RESOURCES.keys()
  farm_type = random.randrange(0, farm_resources_keys)
  for _resource in FARM_RESOURCE[farm_type].keys():	
    FARM_RESOURCE[farm_type][_resource] -= 0.5

def two_index():
  ''' Trigger event for decision of index 2 
      Increase resource-limit of a random farm type '''
  global FARM_RESOURCES
  farm_resources_keys = FARM_RESOURCES.keys()
  farm_type = random.randrange(0, farm_resources_keys)
  for _resource in FARM_RESOURCE[farm_type].keys():	
    FARM_RESOURCE[farm_type][_resource] += 0.5
  	
def three_index():
  ''' Trigger event for decision of index 3 
      Decrease farm growth rate '''
  global FARM_GROWTH_RATE
  farm_type = random.randrange(0, len(FARM_GROWTH_RATE))
  FARM_GROWTH_RATE[FARM_GROWTH_RATE.keys()[farm_type]] -= 0.5

def four_index():
  ''' Trigger event for decision of index 4 
      Increase farm growth rate '''
  global FARM_GROWTH_RATE
  farm_type = random.randrange(0, len(FARM_GROWTH_RATE))
  FARM_GROWTH_RATE[FARM_GROWTH_RATE.keys()[farm_type]] += 0.5

def five_index():
  ''' Trigger event for decision of index 5 
      Delete random forest unit '''
  global _forest_units
  random_forest_unit = random.randrange(0, len(_forest_units))
  _forest_unit = _forest_units[random_forest_unit]
  x = _forest_unit.location.center[0]
  y = _forest_unit.location.center[1]
  delete_location(x,y)
  _forest_units = _forest_units[:random_forest_unit] + _farm_units[random_forest_unit+1:]

def get_prediction():
  ''' Forms the hyperplane by performing a multivariate logistic regressionover the training data collected from the training data '''
  global training_data
  if len(training_data) in [0,1]:
    return 0
  current_params = training_data[-1]
  training_data = training_data[:-1]
  # Multivariate logistic regression using gradient descent
  alpha = 1
  theta = [0] * (len(training_data[0])-1)
  _iterations = 10
  for i in range(_iterations):
    for j in range(0, len(theta)):
      zero_index_cost_diff = 0
      cost_diff = 0
      for _sample in training_data:
        h = sum([theta[x]*_sample[x] for x in range(len(theta))])
        zero_index_cost_diff += (h - _sample[-1])
        cost_diff += ((h - _sample[-1]) * _sample[j])
      cost_diff = (cost_diff*alpha) / len(training_data)
      zero_index_cost_diff = (zero_index_cost_diff*alpha) / len(training_data)
      if j == 0:
        theta[j] = theta[j] - (alpha*zero_index_cost_diff)
      else:
        theta[j] = theta[j] - (alpha*cost_diff)
  prediction = sum([theta[x]*current_params[x] for x in range(len(theta))])
  training_data = []
  if x>5 or x<0:
    x=5
  return x

def update_learning():
  ''' Triggers a game-event based on the user-decision prediction '''
  prediction = get_prediction()
  if prediction == 0:
    zero_index()
  elif prediction == 1:
    one_index()
  elif prediction == 2:
    two_index()
  elif prediction == 3:
    three_index()
  elif prediction == 4:
    four_index()
  elif prediction == 5:
    five_index()


