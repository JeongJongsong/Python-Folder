# 외부파일에 있는거 불러오려면 import 필수
# 실제 사용할때도 다써야함
#  style 1)
# import animal.pet # 불러오는 식 = import 패키지명.모듈명
# d = animal.pet.Dog("후추") # 패키지명.모듈명.클래스명 ......
# d.Bark()
# d.printInfo()

#  style 2)
# import animal.pet as ap #  import 패키지명.모듈명 as 별칭  ->별칭은 변수명처럼 내맘대로 설정
# d = ap.Dog("후추")      # 별칭.클래스명.......
# d.Bark()
# d.printInfo()

#  style 3)
from animal.pet import Dog  # from 패키지명.모듈명 import 가져올것? 
d = Dog("후추")             # 별칭.클래스명.........
d.Bark()
d.printInfo()

#  -> 주로 3번 스타일 사용하겠지만 1, 2도 활용해야함
class Dog:
    pass
d2 = Dog()

# Windows에서PYTHONPATH를 설정하면 프로젝트도 패키지처럼 인식해서.........
# 