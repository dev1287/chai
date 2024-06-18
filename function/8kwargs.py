#def print_kwargs(name, power):
    #print("Name:", name, "Power", power)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
     print(f"{key}:{value}")

  

print_kwargs(name="namesssss", power="lazer")
print_kwargs(name="namesssss2")
print_kwargs(name="namesssss3", power="lazer3", enemy="enem").table()
