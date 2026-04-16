#LAB 6-1
print("LAB 6-1")

#1
print("#1")
capital_dic = {"Korea" : "Seoul", "China" : "Beijing", "USA" : "Washington DC"}
print(capital_dic["Korea"])
print(capital_dic["China"])
print(capital_dic["USA"])

#2
print("#2")
fruits_dic = {"apple" : "5000", "banana" : '4000', "grape" : "5300", "melon" : "6500"}
keys = fruits_dic.keys()
values = fruits_dic.values()
for i in range (4) :
    print(keys, "의 가격은 ", values, "원 입니다.")
print()

#LAB 6-2
print("LAB 6-2")

#1
print("#1")
person = {"이름" : "홍길동", "나이" : "26", "몸무게" : "82"}
person["특기"] = "분신술"
print(person)

#2
print("#2")
person["아버지"] = "홍판서"
print(person)

#3
print("#3")
del person["나이"]
print(person)
print()

#LAB 6-3
print("LAB 6-3")

#1
print("Korea" in capital_dic)
print("China" in capital_dic)
print("Indonesia" in capital_dic)
print("Beijing" in capital_dic)
print()

#LAB 6-4
print("LAB 6-4")
#1
print("#1")
fruits_dic = {"apple" : "6000", "melon" : '3000', "banana" : "5000", "orange" : "7000"}
print(fruits_dic)

#2
print("#2")
print(fruits_dic.keys())

#3
print("#3")
print(fruits_dic.values())

#4
print("#4")
print(fruits_dic.pop("apple"))

#5
print("#5")
print(fruits_dic.clear())
print()

#LAB 6-5
print("LAB 6-5")

#1
print("#1")
fruits_dic = {"apple" : "6000", "melon" : '3000', "banana" : "5000", "orange" : "4000"}
a = list(fruits_dic.keys())
print(a)

#2
print("#2")
b = list(fruits_dic.values())
print(b)

#3
print("#3")
c = len(fruits_dic)
print("fruits_dic 딕셔너리의 항목의 개수 :", c)

#4
print("#4")
if "apple" in fruits_dic :
    print("apple is in fruits_dic")
if "mango" not in fruits_dic :
    print("mango is not in fruits_dic")

#LAB 6-6
print("LAB 6-6")

#1
print("#1")
the_day = (1919, 3, 1)
print("{}년 {}월 {}일은 삼일절입니다.".format(the_day[0], the_day[1], the_day[2]))


#2
print("#2")
list_a = [10, 20, 30]
tuple_a = (list_a, )
k = list_a[::-1]
print("a =", k[0])
print("b =", k[1])
print("c =", k[2])
print()

#LAB 6-7
print("LAB 6-7")

#1
print("#1")
person = ("홍길동", 2019001, 179)
print(person)

#2
print("#2")
print("TypeError: 'tuple' object does not support item assignment")

#3
print("#3")
list_person = list(person)
list_person[1] = 2020003
tuple_person = (list_person,)
print("학번 변동 후 person =", tuple_person)
print()

#LAB 6-8
print("LAB 6-8")

#1
print("#1")
def square(x, y) :
    num1 = int(x)**2
    num2 = int(y)**2
    return num1, num2 
x = input("숫자를 입력하세요 :")
y = input("숫자를 입력하세요 :")
num1, num2 = square(x, y)
print("{}제곱 = {}, {}제곱 = {}".format(x, num1, y, num2))

#2
print("#2")
print((10, 20, 30) + (40, 50, 60))

#3
print("#3")
print("Hello" * 3)
print(("Hello",) * 3)
print("위에는 문자열이 반복 되고, 밑에는 튜플 자체가 반복된다.")
print()

#LAB 6-9
print("LAB 6-9")

#1
print("#1")
lst = ["apple", "mango", "banana"]
s1 = set(lst)
print(s1)

#2
print("#2")
greet = "Good Afternoon"
s2 = set(greet)
print(s2)
print()

#LAB 6-10
print("LAB 6-10")

#1
print("#1")
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60, 70}
print("1)", s1|s2)
print("2)", s1&s2)
print("3)", s1-s2)
print("4)", s1^s2)
print("5)", s1.issubset(s2))
print("6)", s1.issuperset(s2))
print("7)", s1.isdisjoint(s2))
