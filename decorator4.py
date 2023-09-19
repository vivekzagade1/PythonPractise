class CallCount:
    def __int__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount()
def hello(name):
    print('Hello {}'.format(name))


hello('dfdsfdf')
hello('oinofgnh')

print(hello.count)
