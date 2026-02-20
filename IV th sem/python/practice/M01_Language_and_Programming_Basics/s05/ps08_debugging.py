
try:
    a=int(input("Enter a"))
    print(10/a)
except ZeroDivisionError:
    print("cannot didvisble by zero")
except ValueError:
    print("invalid input")
    import pdb
    def add(a, b):
        pdb.set_trace()
        return a+b
    a=int(input("Enter a"))
    b=int(input("Enter b"))
    print (add(a, b))