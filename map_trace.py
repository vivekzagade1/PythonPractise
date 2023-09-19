class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('calling {} '.format(f))
            return f(*args, **kwargs)
        return wrap


result = map(Trace()(ord), 'THe sdsad sdfdf dsf')
print(result)

print(next(result))
