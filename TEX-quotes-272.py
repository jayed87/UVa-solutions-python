c = 0
while True:
    try:
        s = input()
    except EOFError:
        break
    a = []
    for i in s:
        if i =="\"":
            if c == 0:
                a.append("``")
                c = 1
            else:
                a.append("''")
                c = 0
        else:
            a.append(i)
    print("".join(a))