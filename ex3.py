menu = int(input("Assignment number?\n"))
while menu != 0:
    if menu == 1:
        l1 = list(map(int, input("first list of numbers:\n").split()))
        l2 = list(map(int, input("second list of numbers:\n").split()))
        if all((l1[i]**2 == l2[i]) for i in range(len(l1))):
            print(list(map(lambda x, y: x + y, l1, l2)))
        else:
            print("Lists are not interesting\n")

    elif menu == 2:
        def getint(x):
            try:
                return int(x)
            except ValueError:
                return x

        print(list(filter(lambda x: isinstance(x, int), list(map(getint, input("First list:\n").split())))))
    elif menu == 3:
        l1 = []
        for x in range(500):
            if (x % 5 == 0) | (x % 7 == 0):
                l1 += [x]
        for i, l in enumerate(l1):
            print(i, l)
    elif menu == 4:
        def add(op1, op2):
            return op1 + op2

        def sub(op1, op2):
            return op1 - op2

        def mul(op1, op2):
            return op1 * op2

        def div(op1, op2):
            return op1 / op2

        def idiv(op1, op2):
            return op1 // op2

        def rem(op1, op2):
            return op1 % op2

        def exp(op1, op2):
            return op1 ** op2

        funcs = [add, sub, mul, div, idiv,rem, exp]
        x1, x2 = map(int, input("enter 2 integers:\n").split())
        print(list(map(lambda y: y(x1, x2), funcs)))
    else:
        menu = int(input("Error. Try again:\n(0 to quit)\n"))
    menu = int(input("Assignment number?\n"))