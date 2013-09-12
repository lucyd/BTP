class unit_location:
  ''' A location of an unit'''
  def __init__(self):
    self.center = (None, None)

  def set_center(x, y):
    self.center = (x, y)


class farm_unit:
  ''' The farm unit class '''
  def __init__(self, _type=None):
    if _type == None or _type.strip() == '':
      self.farm_type = DEFAULT_FARM_TYPE
    else:
      self.farm_type = _type
    self.location = assign_random_location("farm")
    self.age = 0
    
  def change_location(loc):
    self.location = loc

  def change_type(_type):
    # _type is a valid farm unit type
    self.farm_type = _type


class forest_unit:
  ''' The forest unit class '''
  def __init__(self):
    self.location = assign_random_location("forest")
    #self.resources = DEFAULT_FOREST_RESOURCES
    self.resources = assign_random_resources()

  def change_location(loc):
    self.location = loc

  def fill_resources(resources_dict):
    self.resources = resources_dict



