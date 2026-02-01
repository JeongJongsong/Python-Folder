# Controller
#   상황 판단해서, M이 필요하면 M꺼내고, V필요하면 V꺼내고 그런 역할
#   프로그램 전체의 진입점
#  PL급 back-end 개발자
from p03_M import Calculator
from p03_V import ConsoleScreen


if __name__ == "__main__": #->실행은 여기서 실행해라
    x, y = ConsoleScreen.getXY()
    c = Calculator.getHab(x, y)
    ConsoleScreen.printResult(c)
