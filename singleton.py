def _Base(cls, *args, **kwargs):
  @classmethod
  @property
  def instance(mcls):
    return mcls(*args, **kwargs)

  @staticmethod
  def getInstance(): return instance

  newcls = type(
    f'Singleton_{cls.__name__}', (cls,), {
      'instance': instance,
      'getInstance': getInstance
    }
  )

  return newcls

Singleton = lambda cls: _Base(cls)
Instance = lambda *args, **kwargs: (lambda cls: _Base(cls, *args, **kwargs))
