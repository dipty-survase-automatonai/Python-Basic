a={1,2,3,4}
b={3,4}

def super(a,b):
        for x in b:
            if x not in a:
                print("b is not subset")
                break
        else:
           print("a is superset")
        return

super(a,b)