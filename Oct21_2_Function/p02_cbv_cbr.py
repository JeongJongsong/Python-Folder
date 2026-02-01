# cbv = Call by value, cbr = Call by reference
# Python은 Call by reference(주소값/참조값만) 있음
d = 10
e = 10
#************************************************
def test(a, b, c):
    global e # 지금부터 이 공간에서 e라고하면 4번줄의 그 e
    print(a, b[0], c[0]) # 실행순서 2
    print(id(a), id(b), id(c))
    a = 100
    b[0] = 100 # -> 얘는 함수 밖에 값(기존 값)을 직접 바꾸는거라 마지막 결과값이 바껴나옴
    #   -> list는 값을 참조해서(reference) -> 가변됨
    c = [100, 200] # c값을 새로 만든거
    d = 100 #새로만든 값 -> 어캐알아? 함수명 test에 a,b,c 만있으니까 3번줄 d랑 상관 x
    e = 100 #새로만든 값 -> 어캐알아? 함수명 test에 a,b,c 만있으니까 4번줄 e랑 상관 x
    print(a, b[0], c[0], d, e) # 실행순서 3
    print(id(a), id(b), id(c))
# ***************************************************
a = 10
b = [10, 20]
c = [10, 20]
print(id(a), id(d), id(e)) 
# -> 각각 다른 주소일탠디?? 이거 3개 주소는 왜 같음?? 왜?? 왜띠발??? 셋다 값이 10
# Python이 다 같은 데이터(값)인가 싶어서 주소 같게 나옴
# -> 하나만 만들어서 같이 사용함 -> 굳이?
print(a, b[0], c[0])  # 실행순서 1
print(id(a), id(b), id(c))
test(a, b, c)
print(a, b[0], c[0], d, e) # 실행순서 4
print(id(a), id(b), id(c))






