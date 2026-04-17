student1 = {"name" : "민수", "score" : 85}
student2 = {"name" : "지영", "score" : 92}

def get_grade(student) :
    if student["score"] >= 90 :
        return "A"
    elif student["score"] >= 80 :
        return "B"
    else :
        return "C"

print(get_grade(student1))
print(get_grade(student2))

# 위 코드를 클래스 함수로 변경 ----------------------------------------------

class Student:
    # __init__ 은 class를 초기화 하는 함수 , self는 자기 자신
    def __init__(self, name, score) :
        self.name = name
        self.score = score

    def get_grade(self) :
        if self.score >= 90 :
            return "A"
        elif self.score >= 80 :
            return "B"
        else :
            return "C"

민수 = Student("민수", 85)
지영 = Student("지영", 92)

print(민수.get_grade())
print(지영.get_grade())

'''
민수.name = name
민수.score = score
'''

#--------------------------------------------------------------

class Phone :
    def __init__(self, brand, battery) :
        self.brand = brand
        self.battery = battery
     
    def status(self) :
        print(f"기종 : {self.brand} / 배터리 잔량 : {self.battery}%")
    
    def use(self, minutes) :
        self.battery -= 0.5 * int(minutes)
        a = self.battery
        print(a)

    def charge(self, minutes) :
        self.battery += minutes
        b = self.battery
        print(b)

#my_phone = 이걸 안 해주면 my_phone 이 정의가 안 돼서 밑에꺼 실행 안됨.
my_phone = Phone("Galaxy", 80)

# 여기까지가 my_phone까지 정의 해주는 코드

my_phone.status()
my_phone.use(30)
my_phone.charge(20)

# use (minutes) / charge(minutes) : 사용 가능 시간 / 충전시간
# battery -= 0.5 minutes, battery += minutes
