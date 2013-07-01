class unit_location:
  ''' A location of an unit consisting of a list of 4 tuples '''
  def __init__(self):
    self.top_left = (None, None)
    self.bottom_left = (None, None)
    self.top_right = (None, None)
    self.bottom_right = (None, None)

  def fill(tl, bl, tr, br):
    self.top_left = tl
    self.bottom_left = bl
    self.top_right = tr
    self.bottom_right = br


class farm_unit:
  ''' The farm unit class '''
  def __init__(self):
    self.farm_type = DEFAULT_FARM_TYPE
    self.location = assign_random_location("farm")
    self.age = 0
    
  def change_location(loc):
    # loc is a list of 4 tuples indicating farm unit's boundaries
    self.location = loc

  def change_type(_type):
    # _type is a valid farm unit type
    self.farm_type = _type


class forest_unit:
  ''' The forest unit class '''
  def __init__(self):
    self.location = assign_random_location("forest")
    self.resources = DEFAULT_FOREST_RESOURCES

  def change_location(loc):
    # loc is a list of 4 tuples indicating forest unit's boundaries
    self.location = loc

  def fill_resources(resources_dict):
    self.resources = resources_dict



