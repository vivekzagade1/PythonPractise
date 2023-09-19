def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap


@escape_unicode
def norther_city():
    return 'Troms♂'


print(norther_city())