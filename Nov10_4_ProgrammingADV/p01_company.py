# 입력받은 회사정보를 형변해주쟛

class Company:
    def __init__(self, name, boss, head, employee):
        self.name = name
        self.boss = boss
        self.head = head
        self.employee = int(employee)