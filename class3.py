class Student:
    # __init__ 은 class를 초기화 하는 함수 , self는 자기 자신
    def __init__(self, name, score) :
        self.__name = name
        self.__score = score

    def __str__(self) :
        return f"이름 : {self.__name} / 점수 : {self.__score}"


    def get_grade(self) :
        if self.__score >= 90 :
            return "A"
        elif self.__score >= 80 :
            return "B"
        else :
            return "C"

민수 = Student("민수", 85)
지영 = Student("지영", 92)

print(민수.get_grade())
print(지영.get_grade())

print(민수)
print(민수.__name)


'''
민수.name = name
민수.score = score
'''

