import random

list=[random.randint(0,200)]

for i in range(20):
    list.append(random.randint(0,200));

print(list)
change = True
while change==True:
    change = False
    for x in range(len(list)):

        if x == (len(list)-1):
            print("reached end of list")
            break
        curruntno=list[x]
        next=list[x+1]

        if curruntno > next:
            print("Swap",curruntno,"and",next)
            list[x] = next
            list[x+1] = curruntno
            change=True

print("all finished")
print(list)
