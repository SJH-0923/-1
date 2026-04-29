class Vector2D :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def __str__(self) :
        return "({}, {})".format(self.x, self.y)
    def __add__(self, other) :
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self,other) :
        return Vector2D(self.x - other.x, self.y - other.y)
    def __mul__(self, other) :
        return self.x * other.x + self.y * other.y
    def __lt__(self, other) :
        return self.x**2 + self.y**2 > other.x**2 + other.y**2


v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
#v3 = v1.add(v2)
v3 = v1 + v2 #__add__를 해서 연산 기호로 가능하게 한 코드
v4 = v1 - v2
v5 = v1 * v2
if (v1<v2) :
    print("v1<v2")
print('v1.add(v2) =', v3)
print(v4)
print(v5)
