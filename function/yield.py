def gen_even(limit):
#    li = []
#    for i in range(2, limit+1 ,2):
#        li.append(i)
#    return li
    for i in range(2, limit+1 ,2):
         yield i


#print(gen_even(10))

for num in gen_even(10):
     print(num)

