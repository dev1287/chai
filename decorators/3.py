def f1(fun):
    def wrapper():
        print("started")
        fun()
        print("ended")
    return wrapper


def f():
    print("Hello")


f1(f)()
