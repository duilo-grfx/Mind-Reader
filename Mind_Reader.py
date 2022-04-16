def main():
    a = input("""I can read your mind. 
    Click enter""")
    A = input("""+ = addition
- = subtraction
* = multiplication
/ = division
Clcik enter""")
    b = input("Pick a positive number from 1-30 ")
    bb = eval(b)
    print(bb)
    c = input("multiply it by the same number you chose(Square it) ")
    cc = eval(c)
    print(cc)
    d = input("Add the result to the orginal number ")
    dd = eval(d)
    print(dd)
    e = input("Divide by the original number ")
    ee = eval(e)
    print(ee)
    f = input("Add 17 ")
    ff = eval(f)
    print(ff)
    g = input("subtract by the original number ")
    gg = eval(g)
    print(gg)
    h = input("divide by six ")
    hh = eval(h)
    print(hh)
    i = input("Did you get 3? ")
    if(i == "yes") or (i == "Yes") or (i == "YES"):
        print("I knew I can read your mind")
    elif(i == "no") or (i == "No") or (i == "NO"):
        print("Better luck next time")
    j = input("Do you want to play again?")
    if(j == "yes") or (j == "Yes") or (j == "YES"):
        print("Lets Start! Click enter" for i in range(50))
    elif(j == "no") or (j == "No") or (j == "NO"):
        print("Good bye")
main()

