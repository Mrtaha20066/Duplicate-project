x = input()
def dup(x):
    if len(x) == 0 :
        print("dup")
        return
    elif len(x) % 2 != 0 :
        print("not dup")
        return
    else :
        x = x[0:len(x)//2]
        x = x[1:]
        dup(x)
dup(x)