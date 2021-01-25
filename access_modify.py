import inspect

class AccessException(Exception): pass

def privatefunc(cls, f):
  def _(*args, **kwargs):
    caller = inspect.stack()[1].function
    if not hasattr(cls, caller):
      raise AccessException("Private function cannot be accessed.")
    return f(*args, **kwargs)
  return _

def protectedfunc(cls, f):
  def _(*args, **kwargs):
    mycls = type(args[0])
    if (
      cls != mycls and
      not cls.__name__ in list(map(
        lambda x: x.__name__,
        mycls.__bases__
      ))
    ):
      raise AccessException("Protected function cannot be accessed.")
    return f(*args, **kwargs)
  return _

def access(cls):
  isFunc = lambda f: isinstance(f, type(lambda: 1))
  
  d = dict(cls.__dict__)
  functions = {
    key : d[key] for key in d.keys()
    if isFunc(d[key])
  }
  
  d['__access_modify'] = True
  
  
  for key in functions:
    f = d[key]
    acc = getattr(f, 'access', 'public')
    if acc == 'private':
      d[key] = privatefunc(cls, f)
    elif acc == 'public':
      d[key] = f
    elif acc == 'protected':
      d[key] = protectedfunc(cls, f)
      
  return type(cls.__name__, cls.__bases__, d)


def gen(name):
  def decorator(func):
    setattr(func, 'access', name)
    return func
  return decorator

private = gen('private')
protected = gen('protected')
public = gen('public')


if __name__ == '__main__':
  @access
  class test:
    @private
    def a(self): return 1
    
    @protected
    def b(self): return self.a()+1

  @access
  class qwer(test):
    @public
    def c(self): return self.b()+1
  
  r = test()
  t = qwer()
  
  try: print(r.a())
  except AccessException as e:
    print(f'r.a() is private!')
  
  try: print(r.b())
  except AccessException as e:
    print(f'r.b() is protected!')
  
  print(f't.c() = {t.c()}')
