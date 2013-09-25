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
      self._type = DEFAULT_FARM_TYPE
    else:
      self._type = _type
    self.location = assign_random_location("farm")
    self.age = 0
  
  def change_location(self, loc):
    self.location = loc

  def change_farm_type(self, _type):
    # Assuming _type is in VALID_FARM_TYPES
    self._type = _type

  def get_location(self):
    return self.location

  def get_farm_type(self):
    return self._type

class industry:
  ''' The industrial unit class '''
  def __init__(self, _type=None):
    if _type == None or _type.strip() == '' \
	      or _type not in VALID_INDUSTRY_TYPES:
      self._type = DEFAULT_INDUSTRY_TYPE
    else:
      self._type = _type
    self.location = assign_random_location("industry")
    self.age = 0
    self.gross_product = 0

  def get_location(self):
    return self.location

  def change_location(self, loc):
    self.location = loc
	
  def get_industry_type(self):
    return self._type

  def change_industry_type(self, _type):
    # Assuming _type is in VALID_INDUSTRY_TYPES
    self._type = _type

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

class festival:
  ''' The festival class '''
  def __init__(self):
    self.start_time = 0
    self.duration = 0
    self.RESOURCES = assign_random_resources()

  def get_start_time(self):
    return self.start_time

  def get_duration(self):
    return self.duration

  def get_resources(self):
    return self.RESOURCES

  def change_start_time(self, _time):
    self.start_time = _time

  def change_duration(self, _duration):
    self.duration = _duration

  def change_resources(self, _resources):
    if type(_resources) == type({}):
      self.RESOURCES = _resources

class cultural_unit:
  ''' The cultural unit class '''
  def __init__(self):
    self._type = DEFAULT_CULTURAL_UNIT_TYPE
    self.location = assign_random_location("cultural_unit")
    self.age = 0

  def get_location(self):
    return self.location

  def change_location(self, loc):
    self.location = loc

  def get_cultural_unit_type(self):
    return self._type

  def change_cultural_unit_type(self, _type):
    if _type in VALID_CULTURAL_UNIT_TYPES:
      self._type = _type

class house:
  ''' The house class '''
  def __init__(self, _type=None):
    if _type is None or type.strip() == '':
      self._type = DEFAULT_HOUSE_TYPE
    self.location = assign_random_location("house")
    self.age = 0

  def get_location(self):
    return self.location

  def change_location(self, loc):
    self.location = loc

  def get_house_type(self):
    return self._type

  def change_house_type(self, _type):
    if _type in VALID_HOUSE_TYPES:
      self._type = _type

