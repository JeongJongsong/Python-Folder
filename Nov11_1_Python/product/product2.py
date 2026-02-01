# DTO/VO/bean 은 join시킬것 까지 생각해서 만듦
class Product2:
    def __init__(self, no, name, price, cate, s_name, s_addr, s_birthday):
        self.no = no
        self.name = name
        self.price = price
        self.cate = cate
        self.s_name = s_name
        self.s_addr = s_addr
        self.s_birthday = s_birthday

# 굳이 안보여주고싶은 정보는 여기서 삭제 