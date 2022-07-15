line = int(input())
li=[]
while(line):
    try:
        n=int(input())
        sum = 0
        for i in range(n):
            inp = input()
            int_input = list(map(int, inp.split()))
            av = (int_input[0]/int_input[1])*int_input[1]*int_input[2]
            sum=sum+av
        li.append(int(sum))
        line=line-1
    except EOFError:
        break
for a in li:
    print(a)