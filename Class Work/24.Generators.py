def feed(l):
    for i in l:
        yield i

l=['1..100','101..200','201..300','302..400']
load=feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))
