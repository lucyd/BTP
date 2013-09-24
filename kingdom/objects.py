class unit_location:
  ''' A location of an unit'''
  def __init__(self, x=None, y=None):
    self.center = (x, y)

  def set_center(self, x, y):
    self.center = (x, y)

  def get_center(self):
    return self.center

class farm:
  ''' The agricultural unit class '''
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

  def change_farm_type(self, _type):
    # Assuming _type is in VALID_FARM_TYPES
    self.farm_type = _type

  def get_location(self):
    return self.location

  def get_farm_type(self):
    return self.farm_type

class industry:
  ''' The industrial unit class '''
  def __init__(self, _type=None):
    if _type == None or _type.strip() == '' \
	      or _type not in VALID_INDUSTRY_TYPES:
      self.industry_type = DEFAULT_INDUSTRY_TYPE
    else:
      self.industry_type = _type
    self.location = assign_random_location("industry")
    self.age = 0
    self.gross_product = 0

  def get_location(self):
    return self.location

  def change_location(self, loc):
    self.location = loc
	
  def get_industry_type(self):
    return self.industry_type

  def change_industry_type(self, _type):
    # Assuming _type is in VALID_INDUSTRY_TYPES
    self.industry_type = _type

class hospital:
  ''' The hospital unit class '''
  def __init__(self):
    self.location = assign_random_location("hospital")
    self.age = 0

  def get_location(self):
    return self.location

  def change_location(self, loc):
    self.location = loc
	
class school:
  ''' The school unit class '''
  def __init__(self):
    self.location = assign_random_location("school")
    self.age = 0

  def get_location(self):
    return self.location

  def change_location(self, loc):
    self.location = loc

class university:
  ''' The university unit class '''
  def __init__(self):
    self.location = assign_random_location("university")
    self.age = 0

  def get_location(self):
    return self.location

  def change_location(self, loc):
    self.location = loc
