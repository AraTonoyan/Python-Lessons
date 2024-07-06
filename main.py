import time
import math
import json
import random

# print(random.randrange(2, 10)) # [2,10)
# import random as r
# print(r.randrange(2, 10))
# from random import randrange
# print(randrange(2,10))


# import dis
# def foo():
#     print('hello')
#     return 'hi'
# dis.dis(foo) # bayt kod-i veradarcum


# age = '16'
# print(age)
# age2 = 16
# name = 'ara'
# surname = 'tonoyan'

# print("""hello
# world""")
# print('hello\tworld')
# print("hello\nworld")
# print('\\')
# print("I am 59\" tall")
# print('I\'m 16')
# print("1 havasara 1i" if 1 == 1 else "1 havasar chi 1i")
# print("lava" if 1 == 2 else 'lav chi')
# res = 'chisht' if 1 == 1 else 'suta'
# print(res)


# if 4 == 4 and 2 > 2:
#     print(True)
# else:
#     print(False)

# if 4 == 4 or 2 > 2:
#     print(True)
# else:
#     print(False)

# if not 4 == 4:
#     print(True)
# else:
#     print(False)

# if 4 != 4:
#     print(True)
# else:
#     print(False)

# str = "Hello {} {} you are {}".format(name, surname, age)
# print(str)
# print("Hello {} {} you are {}".format(name, surname, age))

# str = f'Hello {name} {surname} you are {age}'
# print(str)

# result = 16 // 3
# print(result)


# tiv1 = float(input('Առաջին թիվը'))
# tiv2 = float(input('Երկրորդ թիվ'))
# result = tiv1 % tiv2
# print("hello \t my \n friend, you answer is",result)

# name = input('mutqagreq dzer anun@ ------')
# age = input('mutqagreq dzer tariq@ ------')
# print('barev {} \n\t\t duq {} tarekan eq'.format(name, age))

# x = 3
# y = 10
# result = y // x  # bajanuma u amboxj mas@ vercnum
# print(type(result))
# print(result)


# x=3
# x += 10
# print(x)

# x = 3
# y = 11
# result = x % y
# print(result)

# s = {1, 2, 3, 4}
# s2 = {2, 4, 6, 7}
# s.add(123)
# s.add('b')
# print(s)
# print(type(s))
# print(123 in s)

# n1 = int(input("Please insert a number: "))
# n2 = int(input("Please insert the number you want to divide by the previous number: "))
# print(n1 % n2)

# x = 'peter go home. then'
# u = x.upper()
# c = x.capitalize()
# t = x.title()

# print(u)
# print(c)
# print(t)


# brand = 'Apple'
# exchangeRate = 1.235235245
# message = '%s The price of this %s laptop %0.2f is %4.2f USD%2d' % ('arara', brand, 1.33933333335, exchangeRate, 1)
# print(message)

# %s stringi hamar
# %d integeri hamar
# % tiv(x) d prabela anum x-(x-i tvanshanner) hat  (oinak %2d)  (mi xosqov x tiv@ ira erkarutyunna isk aveli depqum prabela anum)
# % bar(x) s prabela anum x-(x-i tarer) chap   (orinak %2s)
# % storaketov tiv f  minchev . grac@ ira erkarutyuna(aysinqn erku tox verevi x tiv@ uxaki ketnela hashvum tvanshan), ketic heto grac tiv@ asuma . ic heto qani tiv lini
# (orinak) '%4.2f' %(1.333333333333) stacvuma ' 1.33'


# print('barev {} duq {} tarekan eq'.format('Ara', 15))


# print('barev {2} duq {1} tarekan eq'.format('Ara', 15, 'Karen'))
# {x} x-@ cuyca tali vorerord argument@ vercni


# message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
# print(message)

# verchaketic heto kara grvi s d f nuyn verevi principov


# print(str(11)+str(15))
# print(int('11')+int('11'))
# print(int(3.9999)) # vercnuma amboxj mas@
# print(float(11))
# print(float(11.823))


# def addOne(x):
#     return x + 1


# print(addOne(10))


# def sum(x, y):
#     return x + y
# print(sum(10, 20))


# for x in range(2):
#     print(x)

# for x in range(10, 20+1):
#     print(x)

# for x in range(10, 50+1, 2):
#     print(x)

# for x in range(10, 50 + 1):
#     if x % 2 == 0:
#         print(x)
#     else:
#         pass

# name = input("Ներմուծեք ձեև անունը------------")
# surname = input("Ներմուծեք ձեև ազգանունը-----------")

# if len(name) <= 6 or len(surname) < 6:
#     print("Validation error")
# else:
#     print("Tamama")

# lists = [2, 3, 4, 5, 6, 7]
# for x in lists:
#     print(x)

# mijin tvabanakan
# def average(lists):
#     result = 0
#     for x in lists:
#         result += x
#     return result / len(lists)


# print(average([1, 2, 3, 4, 5, 6, 7]))

# def factorial(x):
#     result = 1
#     for item in range(1, x + 1):
#         result *= item
#     return result

# def factorial(x):
#     res = 1
#     while x > 1:
#         res *= x * (x-1)
#         x -= 2
#     return res
#
# print(factorial(5))


# recursia
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))


# while True:
#     x = int(input("Ներմուծեք այն թիվը որի ֆակտորիալը պետք է հաշվեք"))
#     print(factorial(x))

# setinterval
# x = 0
# while True:
#     x += 1
#     print('(', x, ')', 'I LOVE YOU❤')
#     time.sleep(0.5)

# while True:
#     x = 'I Love You❤'
#     print(x)
#     time.sleep(1)


# numbers = []
# print(type(numbers))
# numbers.append(10)  # sovorakan verchic avelacnuma
# numbers.append(20)
# numbers.insert(1, 21)  # asuma vor texic avelacni
# numbers.pop()  # verchic jnjuma
# numbers.pop(0)  # vor@ vor uzumes jnjuma
# numbers.remove(21)  # jnji en tar@ vor@ mech@ graca
# del numbers[1]
# numbers.insert(0, 9)
# print(numbers)

# math
# x = 1.4
# print(math.floor(x))
# print(math.ceil(x))

# print(math.pi)
# print(math.e)
# print(math.log(8, 2))

# name = input('nermuceq1 dzer anun@ ----')

# name = name.capitalize()

# print('dzer anun@', name, 'e')

# def dzerovCapitalize(name:str):
#     return name[0].upper() + name[1:].lower()


# print(dzerovCapitalize('ArA'))


# def dzerovCapitalize(name):
#     firstLetter = name[0]
#     firstLetter = firstLetter.upper()
#     i = 0
#     str = ''
#     str += firstLetter
#     for x in name:
#         i += 1
#         if i != 1:
#             str += x.lower()
#     return str

# print(dzerovCapitalize("aRRaA"))


# name = 'ara'
# name = name.capitalize()
# name = name.upper()
# name = name.lower()

# people = {'Aram': '16', 'Ara': '15', 'Valod': '17'}
#
# x = sorted(people, reverse=True)


# x = sorted(people, key=people.get)
# print(x)
# people = dict(Ara=15, Aram=16, Valod=17)  # sa nuyn
# verevi gracn e
# print(people)
# del people['Valod']
# people['Ani'] = 90
# print(people)
# for name in people:
#     print(name)
# for name, salary in people.items():
# print(name)
# print(salary)
# for i in people:
#     print('name = {}, age = {}'.format(i, people[i]))
# print(people.get('Armen', "there isn't Armen"))  # ete armen ka tpuma ira Value isk ete chka tpum there isn't Armen
# x = people.get('Armen', False)
# print(x)

# def n_fibonachi(n):
#     ls = []
#     a = 0
#     a1 = 1
#     an = a + a1
#     for _ in range(n):
#         ls.append(an)
#         an = a + a1
#         a = a1
#         a1 = an
#     print(ls)


# num = [98221122, 43859489237, 32708432723]
# people = ['Ara', 'Tsovinar', 'Henri']
# contact = dict(zip(num, people))
# print(contact)
# contact.clear()
# print(contact)

# pets = ['cat', 'dog', 'rabbit', 'hamster']
# for index, mypet in enumerate(pets):
#     print(index, mypet)
# for mypet in pets:
#     print(pets.index(mypet), mypet)

# word = "hello"
# for x in word:
#     print(x)

# counter = 5
# while counter >= 0:
#     print('counter = {}'.format(counter))
#     counter -= 1


# j = 0
# for i in range(1, 8):
#     j += 1
#     print('\ni =', i, 'j =', j)
#     if j == 6:
#         continue  # nuyn break-na uxaki funkcian lriv chi kangnum uxaki sksac cikl@ @tex kangnuma, u ancnum hajord ciklin
#     print('continue')


# try:
#     print("barev")
#     answer = 12 / 0
#     print(answer)
# except ZeroDivisionError as e:  # exeptic heto karanq grenq errori tesak@ orinak (ValueError, TypeError, .... - https://docs.python.org/3/library/exceptions.html )
#     print("mi ban scxala grac(tiv@ 0i chi bajanvum), bayc minchev sxalin hasnel@ normal ashxatela,", e)
# else:
#     print('urish error ka') # else-n ashxatuma erb amboxj try-@ chisht ashxatuma
# finally:
#     print("inch exav exav, karevor@ sax prcav") # kap chuni verev@ incha grac, verjum finally-n meka ashxatuma
#


# newString = "Hello World".replace("World", "Univers")
# print(newString)

# sct1 = {10, 20, 30, 40, 50, 70}
# sct2 = {30, 40, 50, 60, 70}
# print(sct1.intersection(sct2))  # hatum
# print(sct1.union(sct2))  # miavorum
# print(sct1.difference(sct2)) # sct1-um ka sct2-um chka


# students = [
# {"name": "Arman", "surname": "Simonyan", "masks": [5, 2, 3, 5, 3, 1]},
# {"name": "Nina", "surname": "Simonyan", "masks": [4, 2, 3, 5, 3, 2]},
# {"name": "Saty", "surname": "Simonyan", "masks": [3, 2, 3, 5, 3, 6]},
# {"name": "Ani", "surname": "Simonyan", "masks": [2, 2, 3, 5, 3, 1, 8]},
# {"name": "Gexam", "surname": "Simonyan", "masks": [1, 2, 3, 5, 3, 5]},
# ]

# print(students[1]['masks'][0])
# print(students[0:3])
# print(type(students))
# print(type(students[1]))
# print(type(students[1]['masks']))


# people = {"Bob": 20000, "Aram": 320000, "Simon": 100000}
# print(type(people))
# print(people)
#
# people = json.dumps(people, sort_keys=False)  # sarquma str u chi sortavorum, erkrord argument@ chi sortavorum
# print(type(people))
# print(people)
#
# with open("database.txt", "w") as f:
#     f.write('people')
#
# with open('database.txt', 'r') as f:
#     readResult = json.loads(f.read())
#
# print(readResult)
# print(type(readResult))


# def insert(name, pay):
#     with open('database.txt', 'r') as file:
#         dict = json.loads(file.read())
#         dict[name] = pay
#         with open('database.txt', 'w') as f:
#             f.write(json.dumps(dict))


# insert('Karen', 2222)


# def select():
#     with open("database.txt", 'r') as file:
#         dict = json.loads(file.read())
#         return dict


# print(select())


# def delete(name):
#     with open("database.txt", 'r') as file:
#         dict = json.loads(file.read())
#         del dict[name]
#         print(dict)
#         with open('database.txt','w') as f:
#             f.write(json.dumps(dict))

# delete("Aram")


# def update(name, pay):
#     with open("database.txt", 'r') as file:
#         dict = json.loads(file.read())
#         dict[name] = pay
#         with open('database.txt', 'w') as file:
#             file.write(json.dumps(dict))
#
#
# update('Simon', 120000)


# list = ['ara', 12, 12, 12, 'hoooo', 'na', 3.33333, 'i']
# print(list[-2])  # (-)@ verjica hashvum
# print(list[2:5])  # 2ic minchev 4rd tpuma aranc 4i
# print(list[2:]) # 2ic minchev verj tpuma
# print(list[2::2]) # 2ic minchev verj tpuma, qayl@ 2
# print(list[::-1]) # qayl@ hakarak. aysinqn shrjuma
# list[arajin@ asuma vortexc sksac:minchev vortex:qani hat@ mek]
# print(list[-1:-3:-1])

# list2 = list[::]  #copy-a anum
# list3 = list.copy()  #copy-a anum
# print(list2 == list3)

# list.clear()
# print(list)
# print(list.index("hoooo"))
# print(list.count(12))
# list.reverse() # tarsa sarqum
# list[::-1]  # nuynic
# print(list)
# x = list.copy()  # mi hatela sarqum qo uzats popoxakani anunov
# print(x, "\t", list)
# list[2] = 13
# print(list)


# tuple =("Jan","Fab","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec") # sa constant e ev chi kareli poxel vochinch, chpopoxvox datatype
# tuple[1] = 12
# print(type(tuple))
# print(tuple[1])
# print(tuple[1:6])
# print(tuple[-1])


# def sum_num(*num):
#     print(type(num))
#     res = 0
#     for x in num:
#         res += x
#     return res

# print(sum_num(1, 2, 3, 4, 5))


# def total(**library):
#     print(type(library))
#     ras = 0\
#     for x, y in library.items():
#         ras += y
#     return ras


# print(total(TV=20000, phone=4000, computer=250000))

# text = 'afrfsfs|fegfsdfew}ffs|bergsfrd|grefvrdv|'
# x = text.split('|')
# print(x)
# y = '.'.join(x)
# print(y)


# number = '10'
# print(number.isdigit())
# char = 'abc'
# print(char.isalpha())
# print(isinstance(char, str))
# print(isinstance(number, str))


import turtle

# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("red") # foni guyn@
# t.color("black",'green') # 1 argument@ ira guynna, myus@ borderi gun@
# t.begin_fill()
# t.right(90)
# t.forward(150)
# t.right(90)
# t.forward(150)
# t.right(90)
# t.forward(150)
# t.right(90)
# t.forward(150)
# t.circle(60)
# turtle.done() # vor verchum dus chga


# numbers = [1, 7, 2, 4, 8, 3, 9, 34, 34, 12, 54, 64, 612, 434, 564]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# numbers = sorted(numbers)
# print(numbers)
# numbers.sort()
# print(numbers)


# pets = ['cat', 'dog', 'rabbit', 'hamster']
# for index, mypet in enumerate(pets):
#     print(index, mypet)


# random
# chars = '0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*(){}|"<>?/.,;[]'
# res = ''
# while len(res) <= random.randint(8, 16):
#     x = random.choice(chars)
#     while len(res) < 1:
#         if x.isalpha():
#             res += x.upper()
#         else:
#             x = random.choice(chars)
#             continue
#     y = random.choice(chars)
#     res += y

# print(res)

# def sorting(arr, n=0, count=0, newlist=[]):
#     if count == len(arr) - 1:
#         newlist.append(arr[count])
#         newlist.append(n + 1)
#         return newlist
#     if arr[count] == arr[count + 1]:
#         return sorting(arr, n + 1, count + 1, newlist)
#     else:
#         newlist.append(arr[count])
#         newlist.append(n + 1)
#         n = 0
#         return sorting(arr, n, count + 1, newlist)


# print(sorting(["A", "A", 'A', "A", 'b', 'b', 'b', 'c', 'c', 'h', 'h']))


# with open("file.txt", "w") as f:
#     f.write('barev')
# with open("file1.txt", "w") as f:
#     f.write('barev')
# with open("file2.txt", "w") as f:
#     f.write('barev')
# with open("file3.txt", "w") as f:
#     f.write('barev')
# with open("file4.txt", "w") as f:
#     f.write('barev')

# with open("file.txt","r") as f:
#     x = f.readlines()
#     print(x[:3])

# with open("file.txt", "a") as f:
#     f.write('\nnoric barev')

# with open("file.txt","r") as f:
#     x = f.read()
#     print(x)

# with open("file.txt","r") as f:
#     x = f.readlines()
#     print(max(x))

# with open("file.txt","r") as f:
#     x = f.readlines()
#     for line in x:
#         for letter in line:
#             try:
#                 print(int(letter))
#             except ValueError:
#                 pass

# def rec(li=[]):
#     x = input('greq tiv ------ ')
#     if x == "0":
#         li.sort()
#         li.reverse()
#         print(li)
#         return rec()
#     else:
#         li.append(int(x))
#         return rec(li)


# rec()


# x = [1,4,5,23,324,23,324324,324,234,234234,324,234234432,4324,324,234,234,234234]
# x.sort()


"""tnayin2"""

# def chemistry(res=[], last_letter=''):
#     chem = input('please insert a chemical element')
#     if chem in res:
#         print("this element have already been in this game")
#         return chemistry(res)
#     elif chem == '0':
#         return res
#     else:
#         if last_letter == chem[0] or last_letter == '':
#             res.append(chem)
#             last_letter = chem[-1]
#             return chemistry(res, last_letter)
#         else:
#             print("the first letter isn't the same with the previous last letter")
#             print("try again or insert 0 to stop the game")
#             return chemistry(res, last_letter)


# print(chemistry())

"""tnayin3"""

# class TriangleChecker:
#
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = a, b, c
#
#     def is_triangle(self):
#         if type(self.a) != int or type(self.b) != int or type(self.c) != int:
#             print("Нужно вводить только числа!")
#         elif self.a < 0 or self.b < 0 or self.c < 0:
#             print("С отрицательными числами ничего не выйдет!")
#         elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
#             print('Ура, можно построить треугольник!')
#         else:
#             print('Жаль, но из этого треугольник не сделать')
# x = TriangleChecker(3,4,"5")
# x.is_triangle()

# def get_10_lines(name):
#     try:
#         with open(name, 'r') as f:
#             print(f.readlines()[:10])
#     except FileNotFoundError:
#         print("anun@ sxal eq grel")
# get_10_lines("file5.txt")

# 360 astichan shrjum e
# mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# mat1 = mat[-1][::-1]
# mat2 = mat[-2][::-1]
# mat3 = mat[-3][::-1]
# mat4 = mat[-4][::-1]
#
# ls = list()
# ls.append(mat1)
# ls.append(mat2)
# ls.append(mat3)
# ls.append(mat4)
# print(ls)

# hour = int(input("jama@ asa"))
# if hour > 0 and hour < 12:
#     '''grac jamin gumar 8 u asi qanisna linum'''
#     f = input('am or pm?>')
#     if f == 'am':
#         hour += 8
#         if hour > 12:
#             hour -= 12
#             print(f'{hour}. pm')
#         else:
#             print(f"{hour}. am")
#     elif f == 'pm':
#         hour += 8
#         if hour > 12:
#             hour -= 12
#             print(f'{hour}. am')
#         else:
#             print(f"{hour}. pm")
#     else:
#         print('kam am kam pm. Urish ban mi gri')
# else:
#     print('normal jam asa?')

# ls = [x**2 for x in range(1, 10) if foo(x)]
# print(ls)
# x = 11 if 1 == 1 else 12
# print(x)
# print("barev\a")

# prime
# def parz(lim):
#     ls = [x for x in range(2, lim + 1)]
#     for x in ls:
#         for y in ls:
#             if y % x == 0 and y != x:
#                 ls.remove(y)
#     return ls

# def sorting(arr):
#     flag = False
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 flag = True
#                 # tmp=arr[j]
#                 # arr[j]=arr[j+1]
#                 # arr[j+1]=tmp
#             print('hello')
#         if flag == False:
#             break
#     return arr

# def n_fibonachi(n):
#     ls = []
#     a = 0
#     a1 = 1
#     an = a + a1
#     for _ in range(n):
#         ls.append(an)
#         an = a + a1
#         a = a1
#         a1 = an
#     print(ls)


# def pal(word: str, n=0):
#     if word[n] != word[-1 - n]:
#         return False
#     if n <= int(len(word) / 2):
#         return pal(word, n + 1)
#     else:
#         return True

# def my_range(start=0, end=None, step=1):
#     res = []
#     if end == None:
#         end = start
#         start = 0
#     while end > start:
#         res.append(start)
#         start += step
#     return res
# -------------------------------------------------------------------


# def str_check(srt):
#     for i in range(len(srt) - 1):
#         if srt[i] in srt[i + 1:]: return True
#     return False
#
#
# def str_checkk(srt):
#     st = set(srt)
#     if len(st) == len(srt): return False
#     return True
#
#
# def str_checkkk(srt):
#     st = set()
#     for i in srt:
#         if i in srt:
#             return False
#         st.add(i)
#     return True
#
#
# def str_checkkkk(srt):
#     it = 0
#     for i in srt:
#         x = ord(i) - 97
#         pos = 1 << x
#         if it & pos > 0:
#             return False
#         it |= pos
#
#     return True
# -------------------------------------------------------------------



# list comprehension
# ls = [x for x in range(1, 10)]
# ls2 = [x for x in range(1,10) if x % 2 == 0]
# ls3 = [x**2 for x in range(1,10) if x % 2 == 0]
# print(ls)
# print(ls2)
# print(ls3)
# -------------------------------------------------------------------



# generator expression
# gen = (x for x in range(1, 10))
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3
# -------------------------------------------------------------------



# Generator Function
# def simple_generator():
#     for i in range(1, 6):
#         yield i

# x = simple_generator()
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# -------------------------------------------------------------------


# map
# def square(x):
#     return x * x
#
# numbers = [1, 2, 3, 4, 5]
# squared = map(square, numbers)
# print(type(squared))
# print(list(squared))  # Output: [1, 4, 9, 16, 25]
#
#
# def mapp(func, iterabele):
#     res = []
#     for i in range(len(iterabele)):
#         tmp = func(iterabele[i])
#         res.append(tmp)
#     return res
# numbers = [1, 2, 3, 4, 5]
# squared = mapp(square, numbers)
# print(type(squared))
# print(squared)  # Output: [1, 4, 9, 16, 25]
# -------------------------------------------------------------------


# enumerate
# animals = ['cat', 'dog', 'rabbit']
# for index, animal in enumerate(animals):
#     print(index, animal)
# -----------------------------------------
# def enumerate(argument: list, start: int = 0):
#     res = []
#     for i in range(len(argument)):
#         res.append((i + start, argument[i]))
#     return res
# -------------------------------------------------------------------


# filter
# def is_even(n):
#     return n % 2 == 0
#
# numbers = [1, 2, 3, 4, 5, 6]
# filtered = filter(is_even, numbers)
# print(list(filtered))  # Output: [2, 4, 6]
# -------------------------------------------------------------------


# def filterr(function, iterable):
#     res = []
#     if function == None:
#         for i in iterable:
#             if bool(i) == True:
#                 res.append(i)
#         return res
#     else:
#         for i in iterable:
#             if function(i):
#                 res.append(i)
#             return res
#
# numbers = [1, 2, 3, 4, 5, 6]
# filtered = filter(is_even, numbers)
# print(list(filtered))  # Output: [2, 4, 6]
# -------------------------------------------------------------------


# zip
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# zipped = zip(list1, list2)
# print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# def zzipp(*iterabeles):
#     min_len = len(iterabeles[0])
#     res = []
#     for i in range(1, len(iterabeles)):
#         if min_len > len(iterabeles[i]):
#             min_len = len(iterabeles[i])
#     for i in range(min_len):
#         ls = []
#         for iterabele in iterabeles:
#             ls.append(iterabele[i])
#         res.append(tuple(ls))
#     return res
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# zipped = zzipp(list1, list2)
# print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# -------------------------------------------------------------------


# def zipp(*iterabels):
#     res = []
#     min_len = min(len(i) for i in iterabels)
#     for i in range(min_len):
#         item = tuple(item[i] for item in iterabels)
#         res.append(item)
#     return res
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# zipped = zipp(list1, list2)
# print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# -------------------------------------------------------------------


# reduce
from functools import reduce

# def add(x, y):
#     return x + y

# numbers = [1, 2, 3, 4]
# result = reduce(add, numbers)
# print(result)  # Output: 10

# def reducee(func, sequence):
#     x = func(sequence[0], sequence[1])
#     for i in range(1, len(sequence) - 1):
#         x = func(x, sequence[i + 1])
#     return x

# numbers = [1, 2, 3, 4]
# result = reducee(add, numbers)
# print(result)  # Output: 10
# -------------------------------------------------------------------
