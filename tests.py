def f(*args, **kwargs):
     print(args)
     print(kwargs)

f(1,a=1)
a=lambda x:x**2
print(a(2))