#  Model
#   비즈니스 로직(실제 계산)
#   back-end 개발자 + 고객(이랑 소통해야함 만드는데 필요한 정보 for get)

# deep한 파이썬 영역 작성
class Calculator:
    def getHab(x, y):
        x = int(x)
        y = int(y)
        c = x + y
        return c