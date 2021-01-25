class LiveData:
  def __init__(self, value):
    self.listener = None
    self.listening = True
    self.__value = value

  def setListener(self, func):
    self.listener = func
    return self

  @property
  def value(self): return self.__value

  @value.setter
  def value(self, other):
    self.__value = other
    if self.listening and self.listener: self.listener(self.value)
