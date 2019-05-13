def diff(l1,l2):
    for x in l2:
        if x in l1:
            l2.remove(x)
            l1.remove(x)
    l1.extend(l2)
    return(l1)

def main():
    l1 = list(input("Enter List1:"))
    l2 = list(input("Enter List2:"))
    result=diff(l1,l2)
    print(result)

if __name__ == '__main__':
    main()