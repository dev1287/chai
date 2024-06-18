def f1(fun):
    def wrapper(*args,**kwargs):
        print("started")
        #fun(*args,**kwargs)
        val = fun(*args,**kwargs)
        print("ended")
        return val
    return wrapper

@f1
def f(a,b =9):
    print(a,b)
@f1
def add(x,y):
    return x + y

f("hello")
print(add(12,8))