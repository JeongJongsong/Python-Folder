# 메소드 첫번째 파라메터로 self를 넣냐 마냐 - static
# 멤버변수 없다 -> 저장할게없다 -> 객체 안만들어도 된다
# -> 객체를 안만들고 사용가능한 static 메소드

############  단!!!!!!!! DAO는 객체가 필요함 그래서 멤버변수 만들어야함 ############

from math import ceil
from product.product2 import Product2
from product.product import Product
from jeong.jeongDBManager import JeongDBManager

class ProductDAO:
    def __init__(self):
        self.setAllProductCount() #c처음 한번만 조회하는거
        self.productPerPage = 5
            
    def get(self, pageNo, searchTxt):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            
            searchTxt = "%" + searchTxt + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.productPerPage + 1
            end = pageNo * self.productPerPage

            sql = "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, p_no, p_name, p_price, p_cate, p_s_no "
            sql += "    FROM ( "
            sql += "    SELECT * "
            sql += "    FROM nov11_product "
            sql += "    WHERE p_name LIKE '%s' OR p_cate LIKE '%s' " % (searchTxt, searchTxt)
            sql += "    ORDER BY p_name, p_price "
            sql += "    ) "
            sql +=") "
            sql += "WHERE rn >= %d AND rn <= %d" % (start, end)
            cur.execute(sql)

            products = []
            for _, no, name, price, cate, s_no in cur:
                p = Product(no, name, price, cate, s_no)
                products.append(p)
            return products
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return None
        finally:
            JeongDBManager.closeConCur(con, cur)

    def get2(self, pageNo, searchTxt):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            
            searchTxt = "%" + searchTxt + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.productPerPage + 1
            end = pageNo * self.productPerPage

            sql = "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, p_no, p_name, p_price, p_cate, s_name, s_addr, s_birthday "
            sql += "    FROM ( "
            sql += "    SELECT p_no, p_name, p_price, p_cate, s_name, s_addr, s_birthday "
            sql += "    FROM nov11_seller, nov11_product "
            sql += "    WHERE s_no = p_s_no "
            sql += "         AND (p_name LIKE '%s' OR p_cate LIKE '%s') " % (searchTxt, searchTxt)
            sql += "       ORDER BY p_name, p_price "
            sql += "    ) "
            sql +=") "
            sql += "WHERE rn >= %d AND rn <= %d" % (start, end)
            cur.execute(sql)

            products = []
            for _, no, name, price, cate, s_name, s_addr, s_birthday in cur:
                p = Product2(no, name, price, cate, s_name, s_addr, s_birthday)
                products.append(p)
            return products
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return None
        finally:
            JeongDBManager.closeConCur(con, cur)

    def getMaxPriceProduct(self):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            
            sql = "SELECT p_no, p_name, p_price, p_cate, s_name, s_addr, s_birthday "
            sql += "FROM nov11_seller, nov11_product "
            sql += "WHERE s_no = p_s_no "
            sql += "    AND p_price = ( "
            sql += "        SELECT max(p_price) "
            sql += "        FROM nov11_product "
            sql += "    ) "
            sql += "ORDER BY p_name, p_price "
            cur.execute(sql)

            products = []
            for no, name, price, cate, s_name, s_addr, s_birthday in cur:
                p = Product2(no, name, price, cate, s_name, s_addr, s_birthday)
                products.append(p)
            return products
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return None
        finally:
            JeongDBManager.closeConCur(con, cur)

    def getAll(self):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            sql = "select * from nov11_product order by p_name"
            cur.execute(sql)

            products = []
            for no, name, price, cate, p_s_no in cur:
                p = Product(no, name, price, cate, p_s_no)
                products.append(p)
            return products
        
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return None
        finally:
            JeongDBManager.closeConCur(con, cur)

    def getPageCount(self, searchTxt):
        if searchTxt == "":
            productCount = self.allProductCount
        else:
            productCount = self.getProductCount(searchTxt)
        return ceil(productCount / self.productPerPage)

    def getProductCount(self, searchTxt):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            
            searchTxt = "%" + searchTxt + "%"
            sql = "select count(*) from nov11_product "
            sql += "WHERE p_name LIKE '%s' OR p_cate LIKE '%s' " % (searchTxt, searchTxt)
            cur.execute(sql)

            for result in cur:
                return result[0]
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
        finally:
            JeongDBManager.closeConCur(con, cur)

    def reg(self, product):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            sql = "insert into nov11_product " #여기서 띄어쓰기 무조건 해 안그럼 붙어서 나와서 오류뜸
            sql += "values(nov11_seq.nextval, '%s', '%s, '%s', %s)" %(product.name, product.price, product.cate, product.s_no)

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return "등록성공"
            else:
                return "등록 실패"
            
        except Exception as e:
            print(e)
            return "등록 실패"
        finally:
            JeongDBManager.closeConCur(con, cur)

    def setAllProductCount(self): #전체 물건 수 세는 메서드
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            sql = "select count(*) from nov11_product"
            cur.execute(sql)

            for result in cur:
                self.allProductCount = result[0] # allProductCount라는 멤버변수에 숫자 세팅
         
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
        finally:
            JeongDBManager.closeConCur(con, cur)

