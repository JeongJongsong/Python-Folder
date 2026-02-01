# 6
class Monitor:
    pass
#######################

# import 당했을때 말고
# 이 모듈 실행했을때만 나오게
# -> 실질적 파이썬의 메인영역
if __name__ == "__main__": # ->이 부분은 여기 모듈에서만 나옴
    from Oct29_2_OOPModule.p05_oopModule import PaperCup
    p = PaperCup()