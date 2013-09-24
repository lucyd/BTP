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
    size = INDUSTRY_UNIT_SIZE
  elif unit == 'hospital':
    size = HOSPITAL_UNIT_SIZE
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
    industry.gross_product += PRODUCTION_RATE[industry.industry_type]

def create_farms():
  ''' Creates custom farm units '''
  global VALID_FARM_TYPES
  global farms
  global map_contents
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
  global map_contents
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
	return
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

def create_industry():
  ''' Creates custom industry units'''
  global VALID_INDUSTRY_TYPES
  global industries
  global map_contents
  print 'Enter no.of industries to be built: ',
  industries_to_build = input()
  while industries_to_build > 0:
    industries_to_build -= 1
    new_industry = industry()
    print 'Select industry type'
    print_list(VALID_INDUSTRY_TYPES)
    industry_type = input()
    new_industry.change_industry_type(VALID_INDUSTRY_TYPES[industry_type])
    is_location_random = ''
    while is_location_random not in ['Y', 'N']:
      print 'Randomize location? (Y/N) : ',
      is_location_random = raw_input()
    if is_location_random == 'N':
      print 'Enter industry-unit center co-ordinates: '
      x = input()
      y = input()
      if check_map(x,y) is None:
        new_loc = unit_location(x, y)
        new_industry.change_location(new_loc)
        map_contents[new_loc] = 'industry'
      else:
        print 'Oops!!! Location already assigned'
        return
    industries.append(new_industry)

def destroy_industries():
  ''' Destroys specified industry units '''
  global industries
  global map_contents
  print 'Enter no.of industries to destroy: ',
  industries_to_destroy = input()
  while industries_to_destroy > 0:
    industries_to_destroy -= 1
    print 'Enter center coordinates of industry:'
    x = input()
    y = input()
    for i in range(len(industries)):
      if industries[i].location.center == (x,y):
        map_contents.delete_location(x,y)
        industries = industries[:i] + industries[i+1:]
	return
    print 'Industry-unit specified not found'

def change_production_rate():
  ''' Changes the production rates of industries based on user input '''
  global PRODUCTION_RATE
  global VALID_INDUSTRY_TYPES
  print 'Select industry type'
  print_list(VALID_INDUSTRY_TYPES)
  industry_type = input()
  print 'Enter new production-rate: ',
  new_production_rate = input()
  PRODUCTION_RATE[VALID_INDUSTRY_TYPES[industry_type]] = new_production_rate  

def create_hosptials():
  ''' Creates custom hospital units '''
  global hospitals
  global map_contents
  print 'Enter no.of hospitals to be built: ',
  hospitals_to_build = input()
  while hospitals_to_build > 0:
    hospitals_to_build -= 1
    new_hospital = hospital()
    is_location_random = ''
    while is_location_random not in ['Y', 'N']:
      print 'Randomize location? (Y/N) : ',
      is_location_random = raw_input()
    if is_location_random == 'N':
      print 'Enter hospital-unit center co-ordinates: '
      x = input()
      y = input()
      if check_map(x,y) is None:
        new_loc = unit_location(x, y)
        new_hospital.change_location(new_loc)
        map_contents[new_loc] = 'hospital'
      else:
        print 'Oops!!! Location already assigned'
        return
    hospitals.append(new_hospital)

def destroy_hospitals():
  ''' Destroys specified hospital units '''
  global hospitals
  global map_contents
  print 'Enter no.of hospitals to destroy: ',
  hospitals_to_destroy = input()
  while hospitals_to_destroy > 0:
    hospitals_to_destroy -= 1
    print 'Enter center coordinates of hospital:'
    x = input()
    y = input()
    for i in range(len(hospitals)):
      if hospitals[i].location.center == (x,y):
        map_contents.delete_location(x,y)
        hospitals = hospitals[:i] + hospitals[i+1:]
	return
    print 'Hospital-unit specified not found'

def change_treatment_cost():
  ''' Changes the treatment cost of every hospital/infirmary'''
  global TREATMENT_COST
  print 'Enter new treatment cost: ', 
  TREATMENT_COST = input()

def change_tax():
  ''' Changes the tax '''
  global tax
  print 'Enter new tax: ',
  tax = input()

def change_wages():
  ''' Changes the wages '''
  global wages
  print 'Enter new wages: ',
  wages = input()

def change_budget_allocation():
  ''' Changes the budget allocation '''
  

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

def list_industries():
  ''' Lists all the industries '''
  global industries
  if industries == []:
    print 'No industries in the map'
    return
  for industry in industries:
    print "Type:", industry.industry_type, \
          "  Center:", industry.location.center, \
          "  Age:", industry.age, \
          "  Gross product:", industry.gross_product

def list_resources():
  ''' Lists the player's acquired resources '''
  global PLAYER_RESOURCES
  for resource in PLAYER_RESOURCES.keys():
    print resource, ": ", PLAYER_RESOURCES[resource]

def check_production_rates():
  ''' Lists the industries and their production rates '''
  global PRODUCTION_RATE
  print 'Current production rates are as follows: '
  for _industry in PRODUCTION_RATE.keys():
    print _industry, ': ', PRODUCTION_RATE[_industry]

def check_treatment_cost():
  ''' Lists the current treatment cost '''
  global TREATMENT_COST
  print 'Current treatment cost: ', TREATMENT_COST

def check_tax():
  ''' Lists the current tax value '''
  global tax
  print 'Current tax value: ', tax

def check_wages():
  ''' Lists the current wages '''
  global wages
  print 'Current wages: ', wages

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
  elif user_action == 'Change treatment/medicine cost':
    change_treatment_cost()
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
  elif user_action == 'Check production rates':  
    check_production_rates()
  elif user_action == 'Check treatment cost':
    check_treatment_cost()
  elif user_action == 'Check tax':
    check_tax()
  elif user_action == 'Check wages':
    check_wages()
