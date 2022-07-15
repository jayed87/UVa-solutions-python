while True:
    try:
        line = input("Enter a line of char: ")
        l = len(line)
        a=[]
        for c in line:
            if c=="\'":
                a.append(" ")
            else:
                ab= chr(ord(c) - 7)
                a.append(ab)
        print("".join(a))
    except EOFError:
        break
