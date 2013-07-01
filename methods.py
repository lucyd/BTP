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
  while loc in map_contents.keys():
    tl = (random.randrange(0, map_size), random.randrange(0, map_size))
    bl = (tl[0], tl[1]-size
    tr = (tl[0]+size, tl[1])
    br = (tl[0]+size, tl[1]-size)
    loc.fill(tl, bl, tr, br)
  map_contents[loc] = unit
  return loc

def check_unit(loc):
  ''' If loc is allocated in the map, returns the unit allocated to.
      Else, returns None. '''
  if loc in map_contents.keys():
    return map_contents[loc]
  else:
    return None

