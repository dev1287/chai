import random 
age = int(input("enter your age:"))
days = ["Monday","Wednesday"]
day = random.choice(days)
price =  12 if age >= 18 else 8


if day == "Wednesday":
    print(f"As to day is {day} you'r discounted price is ${(price - 2)}")
else:
    print(f"Price of Ticket is ${price}")