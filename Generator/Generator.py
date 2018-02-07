def square():
    for i in range(1,101):
        yield i**2

generator=square()

iterator=iter(generator)

print("manual:",iterator.__next__())
for i in iterator:
    print("loop:",i)
    
