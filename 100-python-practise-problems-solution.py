#problem 1

# li = []
# for i in range(2000, 3201):
#     if i%7==0 and i%5!=0:
#         li.append(str(i)) #used str(i) to join them them using comma. int can't join

# sep_list = ','.join(li)
# print(sep_list)

# problem 2

# while True:
#     try:
#         num = int(input())
#         fac = 1
#         if num == 0:
#             print("0")
#         elif num == 1:
#             print("1")
#         else:
#             for i in range(1, num+1):
#                 fac = fac*i
#             print(fac)
#     except EOFError:
#         break

# problem 3

# while True:
#     try:
#         num = int(input())
#         d = {}
#         for i in range(1, num+1):
#             d[i] = i*i
#         print(d)
#     except EOFError:
#         break

# problem 4

# while True:
#     try:
#         inp = input()
#         l = inp.split(",")
#         t = tuple(l)
#         print(l)
#         print(t)
#     except EOFError:
#         break

# problem 5

# class TestClass:
#     def __init__(self):
#         self.s = ""
#     def getString(self):
#         self.s = input()
#     def printString(self):
#         print(self.s.upper())

# obj = TestClass()
# obj.getString()
# obj.printString()

# problem 6

# import math
# while True:
#     try:
#         c = 50
#         h = 30
#         # d = input()
#         # li = d.split(",")
#         d = [x for x in input().split(",")]
#         li2 = []
#         for i in d:
#             q = round(math.sqrt((2*c*int(i))/h))
#             li2.append(str(q))
#         sep_list = ','.join(li2)
#         print(sep_list)
#         # print(li2)
#     except EOFError:
#         break

# problem 7

# while True:
#     try:
#         input_str = input()
#         dimensions=[int(x) for x in input_str.split(',')]
#         rowNum=dimensions[0]
#         colNum=dimensions[1]
#         multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

#         for row in range(rowNum):
#             for col in range(colNum):
#                 multilist[row][col]= row*col

#         print (multilist)
#     except EOFError:
#         break

# problem 8

# while True:
#     try:
#         lis = [x for x in input().split(",")]
#         lis.sort()
#         sorted_list = ",".join(lis)
#         print(sorted_list)
#     except EOFError:
#         break

# problem 9

# while True:
#     try:
#         case = int(input())
#         list_of_lines = []
#         for i in range(case):
#             l = input()
#             list_of_lines.append(l.upper())

#         for j in list_of_lines:
#             print(j)
#     except EOFError:
#         break

# problem 10

# while True:
#     try:
#         li = [x for x in input().split(" ")]
#         tu = " ".join(sorted(set(li)))
#         print(tu)
#     except EOFError:
#         break

# problem 11

# while True:
#     try:
#         inp = [x for x in input().split(",")]
#         li=[]
#         for i in inp:
#             int_base_2 = int(i,2) #only taking the binary numbers
#             if int_base_2 % 5==0:
#                 li.append(str(i))
#         coma_seperated = ",".join(li)
#         print(coma_seperated)
#     except EOFError:
#         break

# problem 12

# li = []
# for num in range(2000,3001):
#     s = str(num)
#     if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
#         li.append(s)
# print(','.join(li))

# problem 13


# while True:
#     try:
#         s = input()
#         # count_a = 0
#         # count_n = 0
#         d = {"LETTERS":0, "NUMBERS":0}
#         for c in s:
#             if c.isalpha():
#                 # count_a+=1
#                 d["LETTERS"]+=1
#             elif c.isdigit():
#                 # count_n+=1
#                 d["NUMBERS"]+=1
#         print("LETTERS: ", d["LETTERS"])
#         print("Numbers: ", d["NUMBERS"])
#         # print(d)
#     except EOFError:
#         break

# problem 14

# while True:
#     try:
#         tex = input()
#         dictionary = {"UPPER CASE":0, "LOWER CASE":0}
#         for c in tex:
#             if c.isupper():
#                 dictionary["UPPER CASE"]+=1
#             if c.islower():
#                 dictionary["LOWER CASE"]+=1
#         print("UPPER CASE: ", dictionary["UPPER CASE"])
#         print("LOWER CASE: ", dictionary["LOWER CASE"])
#     except EOFError:
#         break

# problem 15

# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print (n1+n2+n3+n4)

# problem 16

# while True:
#     try:
#         # num = 
#         lis = [int(x)*int(x) for x in input().split(",") if int(x)%2!=0]
#         print(lis)
#     except EOFError:
#         break

# problem 17

# netAmount = 0
# while True:
#     s = input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation == 'D':
#         netAmount+=amount
#     elif operation == 'W':
#         netAmount-=amount
#     else:
#         pass
# print(netAmount)

# Problem 18

# while True:
#     try:
#         s = [x for x in input().split(",")]
#         passWords = []
#         # print(s)
#         for p in s:
#             if len(p)>=6 and len(p)<=12:
#                 # print(p)
#                 cap = 0
#                 sm = 0
#                 num = 0
#                 sp = 0
#                 for c in p:
#                     if c.isupper():
#                         cap = 1
#                     elif c.islower():
#                         sm = 1
#                     elif c.isdigit():
#                         num = 1
#                     elif c in ["@","#","$"]:
#                         sp = 1
#                 if cap ==1 and sm == 1 and num==1 and sp==1:
#                     passWords.append(p)
#             else:
#                 pass
#         passWords = ",".join(passWords)
#         print(passWords)
#     except EOFError:
#         break

# import re
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print (",".join(value))

# problem 19
# 
# sorted_list = []
# li = "jayed,23,459"
# sorted_list.append(tuple(li.split(","))) 
# print(sorted_list)

# from operator import itemgetter, attrgetter
# sorted_list = []
# while True:
#     strng = input()
#     if not strng:
#         break
#     sorted_list.append(tuple(strng.split(",")))

# print (sorted(sorted_list, key=itemgetter(1)))

# problem 20

# def putNumbers(n): # a function with yield in it called a generator
#     for i in range(0,n+1):
#         if i%7==0:
#             yield i

# for i in putNumbers(100):
#     print(i)

# problem 21

# import math

# pos=[0,0]
# while True:
#     s = input()
#     if not s:
#         break
#     li = s.split(" ")
#     direction = li[0]
#     movement = int(li[1])
#     # print(direction)
#     # print(movement)
#     if direction == "UP":
#         pos[1]+=movement
#     elif direction == "DOWN":
#         pos[1]-=movement
#     elif direction == "RIGHT":
#         pos[0]+=movement
#     elif direction == "LEFT":
#         pos[0]-=movement
#     else:
#         pass
# dist = int(round(math.sqrt(pos[1]**2+pos[0]**2)))
# print(dist)

# problem 22

# while True:
#     try:
#         line = [x for x in input().split(" ")]
#         words = {}
#         for word in line:
#             if word in words:
#                 words[word]+=1
#             else:
#                 words[word]= 1

#         for key in sorted(words.keys()):
#             print("%s:%d"%(key,words[key]))

#     except EOFError:
#         break

# problem 23

# def squaredNumber(n):
#     return n**2

# while True:
#     try:
#         num = int(input())
#         print(squaredNumber(num))
#     except EOFError:
#         break
