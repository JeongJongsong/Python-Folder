# 4
# class

from p03_oopModule import Mouse


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def show(self):
        print(self.title, self.price)
################################################
# 품명이 로지텍123, 10000원짜리 마우스
# 정보출력해보기

m = Mouse("로지텍123", 10000)
m.showInfo()