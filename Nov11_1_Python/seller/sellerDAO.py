# 메소드 첫번째 파라메터로 self를 넣냐 마냐 - static
# 멤버변수 없다 -> 저장할게없다 -> 객체 안만들어도 된다
# -> 객체를 안만들고 사용가능한 static 메소드

############  단!!!!!!!! DAO는 객체가 필요함 그래서 멤버변수 만들어야함 ############

from math import ceil
from re import search
from seller.seller import Seller
from jeong.jeongDBManager import JeongDBManager


# 한번 총 판매자수 파악하고 : DB서버랑 통신해서 ... -> 이러면 매번 통신해야됨 -> 횟수줄이잣
# -> 처음 한번만 총 수 세고, 변화 일어나면 수동으로 카운팅
class SellerDAO:
    def __init__(self):
        self.setAllSellerCount() #처음 한번만 조회
        self.sellerPerPage = 3

    def get(self, pageNo, searchTxt):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            
            searchTxt = "%" + searchTxt + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.sellerPerPage + 1
            end = pageNo * self.sellerPerPage

            sql = "SELECT * FROM (SELECT rownum AS rn, s_no, s_name, s_addr, s_birthday "
            sql +="     FROM (SELECT * FROM nov11_seller " 
            sql +="     WHERE S_NAME LIKE '%s' OR s_addr LIKE '%s' " % (searchTxt, searchTxt) 
            sql +="     ORDER BY s_name "
            sql +="    ) "
            sql +=") "
            sql += "WHERE rn >= %d AND rn <= %d" % (start, end)
            cur.execute(sql)

            sellers = []
            for _, no, name, addr, birthday in cur:
                s = Seller(no, name, addr, birthday)
                sellers.append(s)
            return sellers
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return None
        finally:
            JeongDBManager.closeConCur(con, cur)

    def getAll(self):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            sql = "select * from nov11_seller order by s_name"
            cur.execute(sql)

            sellers = []
            for no, name, addr, birthday in cur:
                s = Seller(no, name, addr, birthday)
                sellers.append(s)
            return sellers
            # return cur
            # 1) finally 줄에서 닫아서 없어짐
            # 2) V를 작업하는 사람은 Python을 잘 모르는 사람
            # -> 그래서 최대한 쓰기 쉽게 만들어줘야함

        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return None
        finally:
            JeongDBManager.closeConCur(con, cur)

    def getPageCount(self, searchTxt):
        if searchTxt == "":
            sellerCount = self.allSellerCount
        else:
            sellerCount = self.getSellerCount(searchTxt) 
        return ceil(sellerCount / self.sellerPerPage)


    def getSellerCount(self, searchTxt):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            searchTxt = "%" + searchTxt + "%"
            sql = "select count(*) from nov11_seller "
            sql += "WHERE S_NAME LIKE '%s' OR s_addr LIKE '%s'" % (searchTxt, searchTxt)
            cur.execute(sql)

            for result in cur:
                return result[0] # allSellerCount라는 멤버변수에 8 세팅
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return 0
        finally:
            JeongDBManager.closeConCur(con, cur)

    def reg(self, seller):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
           
            sql = "insert into nov11_seller "
            sql += "values(nov11_seller_seq.nextval, '%s', '%s', to_date('%s', 'YYYYMMDD'))" % (seller.name, seller.addr, seller.birthday)
            
            cur.execute(sql)
            
            if cur.rowcount == 1:
                con.commit()
                self.allSellerCount += 1 # 등록 성공하면 allSellerCount 수동으로 1씩 올림
                print(self.allSellerCount)
                return "등록 성공"
            else:
                return "등록 실패"
        
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return "등록 실패"
        finally:
            JeongDBManager.closeConCur(con, cur)

    def setAllSellerCount(self):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            sql = "select count(*) from nov11_seller"
            cur.execute(sql)

            for result in cur:
                self.allSellerCount = result[0] # allSellerCount라는 멤버변수에 8 세팅
         
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
        finally:
            JeongDBManager.closeConCur(con, cur)
            