def assign_random_location(unit):
  ''' Selects a random location from the map and assigns it as the unit '''
  global FARM_UNIT_SIZE
  global INDUSTRY_UNIT_SIZE
  global HOSPITAL_UNIT_SIZE
  global SCHOOL_UNIT_SIZE
  global UNIVERSITY_UNIT_SIZE
  global CULTURAL_UNIT_SIZE
  global HOUSE_SIZE
  global map_size
  global map_contents
  size = 1
  if unit == 'farm':
    size = FARM_UNIT_SIZE
  elif unit == 'industry':
    size = INDUSTRY_UNIT_SIZE
  elif unit == 'hospital':
    size = HOSPITAL_UNIT_SIZE
  elif unit == 'school':
    size = SCHOOL_UNIT_SIZE
  elif unit == 'university':
    size = UNIVERSITY_UNIT_SIZE
  elif unit == 'cultural_unit':
    size = CULTURAL_UNIT_SIZE
  elif unit == 'house':
    size = HOUSE_SIZE
  loc = unit_location()
  while True:
    x = random.randrange(0+size, map_size-size)
    y = random.randrange(0+size, map_size-size)
    loc.set_center(x,y)
    if loc not in map_contents.keys():
      break
  map_contents[loc] = unit
  return loc

def assign_random_resources():
  ''' Returns random dict of available resources '''
  global PLAYER_RESOURCES
  resources = {}
  for _resource in PLAYER_RESOURCES.keys():
    resources[_resource] = random.randrange(0, PLAYER_RESOURCES[_resource])
  return resources

def receive_input_resources():
  ''' Returns a resources dict of received values '''
  global PLAYER_RESOURCES
  resources = {}
  for _resource in PLAYER_RESOURCES.keys():
    resources[_resource] = PLAYER_RESOURCES[_resource] + 10
    while resources[_resource] > PLAYER_RESOURCES[_resource]:
      print 'Enter % amount: '%(_resource)
      resources[_resource] = input()
  return resources

def update_age():
  ''' Updates the age of all the units '''
  global hospitals
  global schools
  global universities
  global cultural_units
  global houses
  for unit in hospitals + schools + universities + \
              cultural_units + houses:
    unit.age += 1

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
  global map_contents
  for loc in map_contents.keys():
    if loc.center == (x,y):
      map_contents.pop(loc, None)

def increment_time():
  ''' Increments game time by 1 '''
  global time
  time += 1

def update_population():
  ''' Updates the total population in the kingdom '''
  global population
  global houses
  global HOUSE_CAPACITY
  population = 0
  for house in houses:
    population += HOUSE_CAPACITY[house._type]

def update_workers_needed():
  ''' Calculates the no.of workers needed for full employment '''
  global workers_needed
  global EMPLOYEES_REQUIRED
  global farms
  global industries
  global schools
  global universities
  global hospitals
  workers_needed = EMPLOYEES_REQUIRED['Tax Office']
  workers_needed += EMPLOYEES_REQUIRED['Trade Office']
  workers_needed += EMPLOYEES_REQUIRED['Construction']
  workers_needed += EMPLOYEES_REQUIRED['Farm'] * len(farms)
  workers_needed += EMPLOYEES_REQUIRED['Industry'] * len(industries)
  workers_needed += EMPLOYEES_REQUIRED['School'] * len(schools)
  workers_needed += EMPLOYEES_REQUIRED['University'] * len(universities)
  workers_needed += EMPLOYEES_REQUIRED['Hospital'] * len(hospitals)
  workers_needed += EMPLOYEES_REQUIRED['Culture'] * len(cultural_units)

def update_employed_population():
  ''' Finds the total population that's employed '''
  global population
  global employed_population
  global workers_needed
  if population <= workers_needed:
    employed_population = population
  else:
    employed_population = workers_needed

def update_budget():
  ''' Updates the budget '''
  global budget
  global tax
  global wages
  global population
  global employed_population
  global import_goods
  global AVAILABLE_IMPORTS
  global export_goods
  global AVAILABLE_EXPORTS
  budget += (tax*population - wages*employed_population)
  for _import in import_goods:
    budget -= (_import[2] * AVAILABLE_IMPORTS[_import[1]][_import[0]])
  for _export in export_goods:
    budget += (_export[2] * AVAILABLE_EXPORTS[_export[1]][_export[0]])

def calculate_diff(_list):
  ''' Returns the diff of elements of _list
      Used in calculation of score '''
  types_dict = {}
  for _element in _list:
    if _element not in types_dict.keys():
     types_dict[_element._type] = 1
    else:
     types_dict[_element._type] += 1
  diff_elements = 0
  for i in range(len(types_dict.keys())):
    for j in range(i+1, len(types_dict.keys())):
      diff_elements += abs(types_dict[types_dict.keys()[i]] \
                     - types_dict[types_dict.keys()[j]])
  return diff_elements

def update_score():
  ''' Updates the player's score '''
  global SCORE
  global farms
  global industries
  global budget
  global established_trade_routes
  global import_goods
  global export_goods
  global festivals
  global cultural_units
  global schools
  global universities
  global houses
  global workers_needed
  # Agriculture score
  SCORE['Agriculture'] = len(farms) - calculate_diff(farms)
  # Industry score
  SCORE['Industry']  = len(industries) - calculate_diff(industries)
  # Health/Safety score
  SCORE['Health/Safety']  = len(hospitals)
  # Finance score
  SCORE['Finance'] = budget
  # Trade score
  SCORE['Trade'] = len(established_trade_routes) + \
                   len(import_goods) + len(export_goods)
  # Culture score
  SCORE['Culture'] = len(festivals) + len(cultural_units) - calculate_diff(cultural_units)
  # Education score
  SCORE['Education'] = len(schools) + len(universities)
  # Residence score
  SCORE['Residence'] = len(houses) - calculate_diff(houses) - workers_needed
 
def simulate_farm_growth():
  ''' Simulates the farm growth '''
  global farms
  global FARM_GROWTH_RATE
  global FARM_LIFE_SPAN
  for farm in farms:
    farm.age += (FARM_GROWTH_RATE[farm._type])
    if farm.age >= FARM_LIFE_SPAN[farm._type]:
      harvest_farm(farms.index(farm))

def simulate_industry_production():
  ''' Simulates the industry production '''
  global industries
  global PRODUCTION_RATE
  for industry  in industries:
    industry.age += 1
    industry.gross_product += PRODUCTION_RATE[industry._type]

def create_farms():
  ''' Creates custom farm units '''
  global VALID_FARM_TYPES
  global farms
  global map_contents
  global ALLOCATED_BUDGET
  global COST
  print 'Enter no.of farms to be built: ',
  farms_to_build = input()
  while farms_to_build > 0:
    farms_to_build -= 1
    if ALLOCATED_BUDGET['Agriculture'] < COST['Farm']:
      print 'XXXXX Out of budget XXXXX'
      return
    new_farm = farm()
    while check_map(new_farm.location.center[0], new_farm.location.center[1]) is not None:
      new_farm.change_location(assign_random_location('farm'))
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
        delete_location(x,y)
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
  _farm_resources = FARM_RESOURCES[farms[farm_index]._type]
  for resource in _farm_resources.keys():
    PLAYER_RESOURCES[resource] += (farms[farm_index].age * _farm_resources[resource])
  delete_location(farms[farm_index].location.center[0], farms[farm_index].location.center[1])
  farms = farms[:farm_index] + farms[farm_index+1:]

def create_industries():
  ''' Creates custom industry units'''
  global VALID_INDUSTRY_TYPES
  global industries
  global map_contents
  global ALLOCATED_BUDGET
  global COST
  print 'Enter no.of industries to be built: ',
  industries_to_build = input()
  while industries_to_build > 0:
    industries_to_build -= 1
    if ALLOCATED_BUDGET['Industry'] < COST['Industry']:
      print 'XXXXX Out of budget XXXXX'
      return
    new_industry = industry()
    while check_map(new_industry.location.center[0], new_industry.location.center[1]) is not None:
      new_industry.change_location(assign_random_location('industry'))
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
  print 'Enter no.of industries to destroy: ',
  industries_to_destroy = input()
  while industries_to_destroy > 0:
    industries_to_destroy -= 1
    print 'Enter center coordinates of industry:'
    x = input()
    y = input()
    for i in range(len(industries)):
      if industries[i].location.center == (x,y):
        delete_location(x,y)
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
  PRODUCTION_RATE[VALID_INDUSTRY_TYPES[industry_type]] = input()

def create_hosptials():
  ''' Creates custom hospital units '''
  global hospitals
  global map_contents
  global ALLOCATED_BUDGET
  global COST
  print 'Enter no.of hospitals to be built: ',
  hospitals_to_build = input()
  while hospitals_to_build > 0:
    hospitals_to_build -= 1
    if ALLOCATED_BUDGET['Health/Safety'] < COST['Hospital']:
      print 'XXXXX Out of budget XXXXX'
      return
    new_hospital = hospital()
    while check_map(new_hospital.location.center[0], new_hospital.location.center[1]) is not None:
      new_hospital.change_location(assign_random_location('hospital'))
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
  print 'Enter no.of hospitals to destroy: ',
  hospitals_to_destroy = input()
  while hospitals_to_destroy > 0:
    hospitals_to_destroy -= 1
    print 'Enter center coordinates of hospital:'
    x = input()
    y = input()
    for i in range(len(hospitals)):
      if hospitals[i].location.center == (x,y):
        delete_location(x,y)
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
  global budget
  global ALLOCATED_BUDGET
  print 'Current budget: ', budget
  allocated = 0
  for domain in ALLOCATED_BUDGET.keys():
    new_budget = budget + 10
    while new_budget > (budget - allocated):
      print 'Enter new budget for ', domain, ' : ',
      new_budget = input()
    allocated += new_budget
    ALLOCATED_BUDGET[domain] = new_budget

def create_trade_route():
  ''' Creates a new trade route '''
  global trade_routes
  global established_trade_routes
  print 'Currently established trade routes:'
  print_list(established_trade_routes)
  if sorted(trade_routes) == sorted(established_trade_routes):
    print 'All available trade routes established'
  else:
    unestablished_trade_routes = []
    for route in trade_routes:
      if route not in established_trade_routes:
        unestablished_trade_routes.append(route)
    print 'Select new trade route'
    print_list(unestablished_trade_routes)
    selected_route = input()
    established_trade_routes.append(unestablished_trade_routes[selected_route])

def remove_trade_route():
  ''' Removes an existing trade route '''
  global established_trade_routes
  print 'Currently established trade routes: '
  print_list(established_trade_routes)
  print 'Select a trade route to remove: ',
  selected_route = input()
  established_trade_routes = established_trade_routes[:selected_route]\
                             + established_trade_routes[selected_route+1:]

def change_export_price():
  ''' Changes export price of goods '''
  global AVAILABLE_EXPORTS
  print 'Current export prices:'
  for export_good in AVAILABLE_EXPORTS.keys():
    print export_good, ": ", AVAILABLE_EXPORTS[export_good].values()[0]
  print 'Select a good to change it\'s export price'
  print_list(AVAILABLE_EXPORTS.keys())
  selected_good = AVAILABLE_EXPORTS.keys()[input()]
  print 'Enter new export price: ',
  new_price = input()
  for kingdom in AVAILABLE_EXPORTS[selected_good].keys():
    AVAILABLE_EXPORTS[selected_good][kingdom] = new_price

def change_import_policy():
  ''' Changes import policy - type and no.of imports '''
  global AVAILABLE_IMPORTS
  global import_goods
  print 'Current import policy'
  for _tuple in import_goods:
    print 'Kingdom: ', _tuple[0], 'Good: ', _tuple[1], 'Number: ', _tuple[2]
  done = 'N'
  while done != 'Y':
    'Done changing import policy?(Y/N): ',
    done = raw_input()
    print 'Select a kingdom: ',
    kingdom_selected = raw_input()
    print 'Select a good: ',
    good_selected = raw_input()
    print 'Enter no.of goods to import: ',
    number_of_goods = input()
    for _tuple in import_goods:
      if _tuple[0] == kingdom_selected and \
         _tuple[1] == good_selected:
        _tuple[2] = number_of_goods

def change_export_policy():
  ''' Changes export policy - type and no.of exports '''
  global AVAILABLE_EXPORTS
  global export_goods
  print 'Current export policy'
  for _tuple in export_goods:
    print 'Kingdom: ', _tuple[0], 'Good: ', _tuple[1], 'Number: ', _tuple[2]
  done = 'N'
  while done != 'Y':
    'Done changing export policy?(Y/N): ',
    done = raw_input()
    print 'Select a kingdom: ',
    kingdom_selected = raw_input()
    print 'Select a good: ',
    good_selected = raw_input()
    print 'Enter no.of goods to export: ',
    number_of_goods = input()
    for _tuple in export_goods:
      if _tuple[0] == kingdom_selected and \
         _tuple[1] == good_selected:
        _tuple[2] = number_of_goods

def arrange_festival():
  ''' Arrange a festival '''
  global time
  global festivals
  global COST
  global ALLOCATED_BUDGET
  if ALLOCATED_BUDGET['Culture'] < COST['Festival']:
    print 'Insufficient budget'
    return
  festival = new_festival()
  print 'Enter start time of festival: ',
  festival.change_start_time(input())
  print 'Enter duration of festival: ',
  festival.change_duration(input())
  print 'Assign random resources?(Y/N) : ',
  assign_random_resources = raw_input()
  if assign_random_resources == 'N':
    festival.change_resources(receive_input_resources())
  festivals.append(festival)

def build_cultural_units():
  ''' Builds cultural units '''
  global VALID_CULTURAL_UNIT_TYPES
  global cultural_units
  global map_contents
  global ALLOCATED_BUDGET
  global COST
  print 'Enter no.of cultural units to be built: ',
  cultural_units_to_build = input()
  while cultural_units_to_build > 0:
    cultural_units_to_build -= 1
    if ALLOCATED_BUDGET['Culture'] < COST['Cultural unit']:
      print 'XXXXX Out of budget XXXXX'
      return
    new_cultural_unit = cultural_unit()
    while check_map(new_cultural_unit.location.center[0], new_cultural_unit.location.center[1]) is not None:
      new_cultural_unit.change_location(assign_random_location('cultural_unit'))
    print 'Select cultural_unit type'
    print_list(VALID_CULTURAL_UNIT_TYPES)
    cultural_unit_type = input()
    new_cultural_unit.change_cultural_unit_type(VALID_CULTURAL_UNIT_TYPES[cultural_unit_type]) 
    is_location_random = ''
    while is_location_random not in ['Y', 'N']:
      print 'Randomize location? (Y/N) : ',
      is_location_random = raw_input()
    if is_location_random == 'N':
      print 'Enter cultural_unit center co-ordinates: '
      x = input()
      y = input()
      if check_map(x,y) is None:
        new_loc = unit_location(x, y)
        new_cultural_unit.change_location(new_loc)
        map_contents[new_loc] = 'cultural_unit'
      else:
        print 'Oops!!! Location already assigned'
        return
    cultural_units.append(new_cultural_unit)

def destroy_cultural_units():
  ''' Destroys specified cultural units '''
  global cultural_units
  print 'Enter no.of cultural_units to destroy: ',
  cultural_units_to_destroy = input()
  while cultural_units_to_destroy > 0:
    cultural_units_to_destroy -= 1
    print 'Enter center coordinates of cultural_unit:'
    x = input()
    y = input()
    for i in range(len(cultural_units)):
      if cultural_units[i].location.center == (x,y):
        delete_location(x,y)
        cultural_units = cultural_units[:i] + cultural_units[i+1:]
	return

def build_schools():
  ''' Builds school units'''
  global schools
  global map_contents
  global ALLOCATED_BUDGET
  global COST
  print 'Enter no.of schools to be built: ',
  schools_to_build = input()
  while schools_to_build > 0:
    schools_to_build -= 1
    if ALLOCATED_BUDGET['Education'] < COST['School']:
      print 'XXXXX Out of budget XXXXX'
      return
    new_school = school()
    while check_map(new_school.location.center[0], new_school.location.center[1]) is not None:
      new_school.change_location(assign_random_location('school'))
    is_location_random = ''
    while is_location_random not in ['Y', 'N']:
      print 'Randomize location? (Y/N) : ',
      is_location_random = raw_input()
    if is_location_random == 'N':
      print 'Enter school center co-ordinates: '
      x = input()
      y = input()
      if check_map(x,y) is None:
        new_loc = unit_location(x, y)
        new_school.change_location(new_loc)
        map_contents[new_loc] = 'school'
      else:
        print 'Oops!!! Location already assigned'
        return
    schools.append(new_school)

def destroy_schools():
  ''' Destroys specified schools '''
  global schools
  print 'Enter no.of schools to destroy: ',
  schools_to_destroy = input()
  while schools_to_destroy > 0:
    schools_to_destroy -= 1
    print 'Enter center coordinates of school:'
    x = input()
    y = input()
    for i in range(len(schools)):
      if schools[i].location.center == (x,y):
        delete_location(x,y)
        schools = schools[:i] + schools[i+1:]
	return

def build_universities():
  ''' Builds university units'''
  global universities
  global map_contents
  global ALLOCATED_BUDGET
  global COST
  print 'Enter no.of universities to be built: ',
  universities_to_build = input()
  while universities_to_build > 0:
    universities_to_build -= 1
    if ALLOCATED_BUDGET['Education'] < COST['University']:
      print 'XXXXX Out of budget XXXXX'
      return
    new_university = university()
    while check_map(new_university.location.center[0], new_university.location.center[1]) is not None:
      new_university.change_location(assign_random_location('university'))
    is_location_random = ''
    while is_location_random not in ['Y', 'N']:
      print 'Randomize location? (Y/N) : ',
      is_location_random = raw_input()
    if is_location_random == 'N':
      print 'Enter university center co-ordinates: '
      x = input()
      y = input()
      if check_map(x,y) is None:
        new_loc = unit_location(x, y)
        new_university.change_location(new_loc)
        map_contents[new_loc] = 'university'
      else:
        print 'Oops!!! Location already assigned'
        return
    universities.append(new_university)

def destroy_universities():
  ''' Destroys specified universities '''
  global universities
  print 'Enter no.of universities to destroy: ',
  universities_to_destroy = input()
  while universities_to_destroy > 0:
    universities_to_destroy -= 1
    print 'Enter center coordinates of university:'
    x = input()
    y = input()
    for i in range(len(universities)):
      if universities[i].location.center == (x,y):
        delete_location(x,y)
        universities = universities[:i] + universities[i+1:]
	return

def build_houses():
  ''' Builds houses '''
  global VALID_HOUSE_TYPES
  global houses
  global map_contents
  global ALLOCATED_BUDGET
  global COST
  print 'Enter no.of houses to be built: ',
  houses_to_build = input()
  while houses_to_build > 0:
    houses_to_build -= 1
    new_house = house()
    while check_map(new_house.location.center[0], new_house.location.center[1]) is not None:
      new_house.change_location(assign_random_location('house'))
    print 'Select house type'
    print_list(VALID_HOUSE_TYPES)
    house_type = input()
    if ALLOCATED_BUDGET['Residence'] < COST[VALID_HOUSE_TYPES[house_type]]:
      print 'XXXXX Out of budget XXXXX'
      return
    new_house.change_house_type(VALID_HOUSE_TYPES[house_type]) 
    is_location_random = ''
    while is_location_random not in ['Y', 'N']:
      print 'Randomize location? (Y/N) : ',
      is_location_random = raw_input()
    if is_location_random == 'N':
      print 'Enter house center co-ordinates: '
      x = input()
      y = input()
      if check_map(x,y) is None:
        new_loc = unit_location(x, y)
        new_house.change_location(new_loc)
        map_contents[new_loc] = 'house'
      else:
        print 'Oops!!! Location already assigned'
        return
    houses.append(new_house)

def destroy_houses():
  ''' Destroys specified houses '''
  global houses
  print 'Enter no.of houses to destroy: ',
  houses_to_destroy = input()
  while houses_to_destroy > 0:
    houses_to_destroy -= 1
    print 'Enter center coordinates of house:'
    x = input()
    y = input()
    for i in range(len(houses)):
      if houses[i].location.center == (x,y):
        delete_location(x,y)
        houses = houses[:i] + houses[i+1:]
	return
    print 'House specified not found'

def list_farms():
  ''' Lists all the farms '''
  global farms
  if farms == []:
    print 'No farms in the map'
    return
  for farm in farms:
    print "Type:", farm._type, \
          "  Center:", farm.location.center, \
          "  Age:", farm.age

def list_industries():
  ''' Lists all the industries '''
  global industries
  if industries == []:
    print 'No industries in the map'
    return
  for industry in industries:
    print "Type:", industry._type, \
          "  Center:", industry.location.center, \
          "  Age:", industry.age, \
          "  Gross product:", industry.gross_product

def list_cultural_units():
  ''' Lists all cultural units '''
  global cultural_units
  if cultural_units == []:
    print 'No cultural units in the kingdom'
    return
  for cult_unit in cultural_units:
    print 'Type:', cult_unit._type, \
          ' Center:', cult_unit.location.center, \
          ' Age:', cult_unit.age

def list_schools():
  ''' Lists all schools '''
  global schools
  if schools == []:
    print 'No schools in the kingdom'
    return
  for _school in schools:
    print ' Center:', _school.location.center, \
          ' Age:', _school.age

def list_universities():
  ''' Lists all universities '''
  global universities
  if universities == []:
    print 'No universities in the kingdom'
    return
  for _university in universities:
    print ' Center:', _university.location.center, \
          ' Age:', _university.age

def list_houses():
  ''' Lists all houses '''
  global houses
  if houses == []:
    print 'No houses in the kingdom'
    return
  for _house in houses:
    print 'Type:', _house._type, \
          ' Center:', _house.location.center, \
          ' Age:', _house.age

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

def check_budget_allocation():
  ''' Prints the current budget allocation details '''
  global budget
  global ALLOCATED_BUDGET
  for domain in ALLOCATED_BUDGET.keys():
    print domain, ' : ', ALLOCATED_BUDGET[domain]
  print 'Total budget : ', budget

def check_score():
  ''' Prints the player's current score '''
  global score
  print 'Current score: ', score

def print_list(_list):
  ''' Prints the contents of _list in an ordered format '''
  if len(_list) == 0:
    print 'None'
  for i in range(len(_list)):
    print i, ": ", _list[i]

def get_user_input():
  ''' Receives the user input '''
  global DOMAINS
  chosen_domain = len(DOMAINS.keys()) + 1
  while chosen_domain >= len(DOMAINS.keys()):
    print 'Select one of the following domains'
    print_list(DOMAINS.keys())
    chosen_domain = input()
  domain_actions = DOMAINS.values()[chosen_domain]
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
  elif user_action == 'Create hospitals/infirmaries':
    create_hospitals()
  elif user_action == 'Destroy hospitals/infirmaries':
    destroy_hospitals()
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
  elif user_action == 'Remove existing trade route':
    remove_trade_route()
  elif user_action == 'Change export price':
    change_export_price()
  elif user_action == 'Change import policy':
    change_import_policy()
  elif user_action == 'Change export policy':
    change_export_policy
  elif user_action == 'Arrange festival':
    arrange_festival()
  elif user_action == 'Build cultural units':
    build_cultural_units()
  elif user_action == 'Destroy cultural units':
    destroy_cultural_units()
  elif user_action == 'List cultural units':
    list_cultural_units()
  elif user_action == 'Build school':
    build_school()
  elif user_action == 'Build university':
    build_university()
  elif user_action == 'Destroy schools':
    destroy_schools()
  elif user_action == 'Destroy universities':
    destroy_universities()
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
  elif user_action == 'Check budget allocation':
    check_budget_allocation()
  elif user_action == 'Check score':
    check_score()
  elif user_action == 'List my resources':
    list_resources()
