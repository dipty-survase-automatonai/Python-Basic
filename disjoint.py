a={1,2,3,4}
b={3,1}

def dis(a,b):
        for x in b:
            if x not in a:
                print("a and b are disjoint")
                break
        else:
           print("a and b are not disjoint")
        return

dis(a,b)
