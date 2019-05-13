l1 = list(input("Enter List1:"))
l2 = list(input("Enter List2:"))
for x in l2:
    if x in l1:
        l2.remove(x)
        l1.remove(x)
l1.extend(l2)
print(l1)
