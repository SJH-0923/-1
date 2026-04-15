class Cat:
    # 생성자혹은초기화메소드라한다
    def __init__(self, name, color='흰색'):
        self.name = name        # name이라는 인스턴스 변수를 생성
        self.color = color      # color라는 인스턴스 변수를 생성
    # 고양이의정보를출력하는메소드
    def meow(self):
        print('내 이름은 {}, 색깔은 {}, 야옹 야옹~~'.format(self.name, self.color))

nabi = Cat('나비', '검정색') # nabi인스턴스생성
nero = Cat('네로', '흰색') # nero인스턴스생성
mimi = Cat('미미', '갈색') # mini인스턴스생성

nabi.meow()
nero.meow()
mimi.meow()
