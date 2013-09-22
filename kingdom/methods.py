def assign_random_location(unit):
  ''' Selects a random location from the map and assigns it as the unit '''
  global FARM_UNIT_SIZE
  global INDUSTRY_UNIT_SIZE
  global map_size
  global map_contents
  size = 1
  if unit == 'farm':
    size = FARM_UNIT_SIZE
  elif unit == 'industry':
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

def check_map(x, y):
  ''' If (x,y) is allocated in the map, returns the unit allocated to.
      Else, returns None. '''
  global map_contents
  for loc in map_contents.keys():
    if loc.center == (x,y):
      return map_contents[loc]
  return None

def delete_location(x, y):
  ''' Removes the location from map_contents '''
  for loc in map_contents.keys():
    if loc.center == (x,y):
      map_contents.pop(loc, None)

def increment_time():
  ''' Increments game time by 1 '''
  global time
  time += 1

def simulate_farm_growth():
  ''' Simulates the farm growth '''
  global farms
  global FARM_GROWTH_RATE
  global FARM_LIFE_SPAN
  for farm in farms:
    farm.age += (FARM_GROWTH_RATE[farm.farm_type])
    if farm.age >= FARM_LIFE_SPAN[farm.farm_type]:
      harvest_farm(farms.index(farm))

def simulate_industry_production():
  ''' Simulates the industry production '''
  global industries
  global PRODUCTION_RATE
  for industry  in industries:
    industry.age += 1
    industry.product += PRODUCTION_RATE[industry.industry_type]

def create_farms():
  ''' Creates custom farm units '''
  global VALID_FARM_TYPES
  global farms
  print 'Enter no.of farms to be built: ',
  farms_to_build = input()
  while farms_to_build > 0:
    farms_to_build -= 1
    new_farm = farm()
    print 'Select farm type'
    print_list(VALID_FARM_TYPES)
    farm_type = input()
    new_farm.change_farm_type(VALID_FARM_TYPES[farm_type]) 
    is_location_random = ''
    while is_location_random not in ['Y', 'N']:
      print 'Randomize location? (Y/N) : ',
      is_location_random = raw_input()
    if is_location_random == 'N':
      print 'Enter farm-unit center co-ordinates: '
      x = input()
      y = input()
      if check_map(x,y) is None:
        new_loc = unit_location(x, y)
        new_farm.change_location(new_loc)
        map_contents[new_loc] = 'farm'
      else:
        print 'Oops!!! Location already assigned'
        return
    farms.append(new_farm)

def destroy_farms():
  ''' Destroys specified farm units '''
  global farms
  print 'Enter no.of farms to destroy: ',
  farms_to_destroy = input()
  while farms_to_destroy > 0:
    farms_to_destroy -= 1
    print 'Enter center coordinates of farm:'
    x = input()
    y = input()
    for i in range(len(farms)):
      if farms[i].location.center == (x,y):
        map_contents.delete_location(x,y)
        farms = farms[:i] + farms[i+1:]
    print 'Farm-unit specified not found'

def harvest_farm(farm_index):
  ''' Remove and harvest a farm unit's resources '''
  global farms
  global FARM_RESOURCES
  global PLAYER_RESOURCES
  if farm_index >= len(farms):
    print 'Farm unit %d not found'%(farm_index)
  _farm_resources = FARM_RESOURCES[farms[farm_index].farm_type]
  for resource in _farm_resources.keys():
    PLAYER_RESOURCES[resource] += (farms[farm_index].age * _farm_resources[resource])
  farms = farms[:farm_index] + farms[farm_index+1:]

def list_farms():
  ''' Lists all the farms '''
  global farms
  if farms == []:
    print 'No farms in the map'
    return
  for farm in farms:
    print "Type:", farm.farm_type, \
          "  Center:", farm.location.center, \
          "  Age:", farm.age

def list_resources():
  ''' Lists the player's acquired resources '''
  global PLAYER_RESOURCES
  for resource in PLAYER_RESOURCES.keys():
    print resource, ": ", PLAYER_RESOURCES[resource]

def print_list(_list):
  ''' Prints the contents of _list in an ordered format '''
  for i in range(len(_list)):
    print i, ": ", _list[i]

def get_user_input():
  ''' Receives the user input '''
  global domains
  chosen_domain = len(domains.keys()) + 1
  while chosen_domain >= len(domains.keys()):
    print 'Select one of the following domains'
    print_list(domains.keys())
    chosen_domain = input()
  domain_actions = domains.values()[chosen_domain]
  user_action = len(domain_actions) + 1
  while user_action >= len(domain_actions):
    print 'Select one of the following actions'
    print_list(domain_actions)
    user_action = input()
  return domain_actions[user_action]

def process_user_input(user_action):
  ''' Takes appropriate action based on user input '''
  if user_action == 'Pass':
    return
  elif user_action == 'Create farms':
    create_farms()
  elif user_action == 'Destroy farms':
    destroy_farms()
  elif user_action == 'List farms':
    list_farms()
  elif user_action == 'Create industries':
    create_industries()
  elif user_action == 'Destroy industries':
    destroy_industries()
  elif user_action == 'List industries':
    list_industries()
  elif user_action == 'Change production rate':
    change_production_rate()
  elif user_action == 'Create hospital/infirmary':
    create_hospital()
  elif user_action == 'Destroy hospital/infirmary':
    destroy_hospital()
  elif user_action == 'List hospitals/infirmaries':
    list_hospitals()
  elif user_action == 'Change treatment/medicine price':
    modify_medicine_price()
  elif user_action == 'Change tax':
    change_tax()
  elif user_action == 'Change wages':
    change_wages()
  elif user_action == 'Change budget allocation':
    change_budget_allocation()
  elif user_action == 'Create new trade route':
    create_trade_route()
  elif user_action == 'Destroy existing trade route':
    destroy_trade_route()
  elif user_action == 'Change export price':
    change_export_price()
  elif user_action == 'Change import policy':
    change_import_policy()
  elif user_action == 'Change export policy':
    change_export_policy
  elif user_action == 'Arrange festival':
    arrange_festival()
  elif user_action == 'Build cultural unit':
    build_cultural_unit()
  elif user_action == 'Build school':
    build_school()
  elif user_action == 'Build university':
    build_university()
  elif user_action == 'Destroy school':
    destroy_school()
  elif user_action == 'Destroy university':
    destroy_university()
  elif user_action == 'List schools':
    list_schools()
  elif user_action == 'List universities':
    list_universities()
  elif user_action == 'Build houses':
    build_houses()
  elif user_action == 'Destroy houses':
    destroy_houses()
  elif user_action == 'List houses':
    list_houses()
  elif user_action == 'Check population':
    check_population()
    
