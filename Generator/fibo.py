def fibo():
    x=1
    yield x
    y=1
    yield y
    while True:
        x,y=y,y+x
        yield y

generator=fibo()
iterator=iter(generator)
while True:
    ans=input("go:(Y/N):")
    if(ans.upper()=="Y"):
        print(iterator.__next__())
    else:
        break
