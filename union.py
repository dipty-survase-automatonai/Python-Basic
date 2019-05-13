l1 = list(input("Enter List1:"))
l2 = list(input("Enter List2:"))
l3 = l1
for x in l2:
    if x not in l1:
        l3.append(x)
print("l1 is {}\n l2 is {}\n")
print(l3)
