def FooBar(n):
    for i in range(1, n+1):
        if i % 5 == 0 and i % 3 == 0:
            print("FooBar")
        elif i % 3 == 0:
            print("Foo")
        elif i % 5 == 0:
            print("Bar")
        else:
            print(i)

FooBar(30)
