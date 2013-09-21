class unit_location:
  ''' A location of an unit'''
  def __init__(self, x=None, y=None):
    self.center = (x, y)

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

  def change_type(self, _type):
    # _type is a valid farm unit type
    self.farm_type = _type

  def get_type(self):
    return self.farm_type

class forest_unit:
  ''' The forest unit class '''
  def __init__(self):
    self.location = assign_random_location("forest")
    #self.resources = DEFAULT_FOREST_RESOURCES
    self.resources = assign_random_resources()
    self.age = 0

  def change_location(loc):
    self.location = loc

  def fill_resources(resources_dict):
    self.resources = resources_dict


