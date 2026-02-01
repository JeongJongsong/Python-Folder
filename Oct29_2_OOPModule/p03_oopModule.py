# 3
# 제목이 점프투파이썬, 가격이 30000인 책
# 정보출력
from p04_oopModule import Book
# class

class Mouse:
    def __init__(self, model, price):
        self.model = model
        self.price = price
    def showInfo(self):
        print(self.model, self.price)

####################################3
b = Book("점프투파이썬", 30000)
b.show()