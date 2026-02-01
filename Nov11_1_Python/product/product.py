# DTO/VO/bean 은 join시킬것 까지 생각해서 만듦
class Product:
    def __init__(self, no, name, price, cate, s_no):
        self.no = no
        self.name = name
        self.price = price
        self.cate = cate
        self.s_no = s_no



        # join 안쓰고 join 하는거 배우고싶다!!!!!!!!!!!!!!!
        # 나중에 존나빅데이터 활용할껀데 join으로 하면 너무 비효울적이니까
        # 위에 기술 당장은 어렵고 이해 안가도 나중에 써먹을것 같긴함