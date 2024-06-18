username = "raghavendra"
  
def func():
    username = "inside function1"
    print(username)


print(username)
func()

x = 99

def fun2(y):
    z = x + y
    return z

resultfun2 = fun2(1)

print(resultfun2)


def fun3():
    global x
    x = 12
fun3()
print(x)


def fun4():
    global x
fun4()
print(x)


print("----------------")
print(x)

print("---------f1 f2-------")

def f1():
    x = 88
    def f2():
        print(x,"from inside")
    f2()
f1()
        
print("---------f1 f2 return closure 1-------")       

def f1():
    x = 88
    def f2():
        print(x,"from inside3")
    return f2
my_result = f1()
my_result()

print("---------f1 f2 return closure 2-------")   
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))