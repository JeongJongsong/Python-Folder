# 밑에꺼 왜 이렇게 씀? 이게 뭐지?
from product.productDAO import ProductDAO
from seller.sellerDAO import SellerDAO
from consoleScreen import ConsoleScreen

# 만든 프로그램을 나 혼자만 사용하는게 아니고, 쇼핑몰 직원들이 같이 사용 
# -> DB계정 하나를 여럿이 사용
# 계정 하나를 동시사용가능 수 정해져있음(100명까지 동시사용가능)
# -> 계정 빨리 쓰고 빨리 끊어야 1000명이 다 사용 가능

if __name__ == "__main__":
    sellerDAO = SellerDAO()
    productDAO = ProductDAO()

    while True :
        menu = ConsoleScreen.showMainMenu()

        if menu == "10":
            break
        elif menu == "1":
            seller = ConsoleScreen.showRegSellerMenu()
            result = sellerDAO.reg(seller)
            ConsoleScreen.showResult(result)
           
            # 판매자 정보 입력받아서 DB에 등록 하는 부분
        elif menu == "2":
            product = ConsoleScreen.showRegProductMenu()
            result = productDAO.reg(product)
            ConsoleScreen.showResult(result)
        
        elif menu == "3":
            sellers = sellerDAO.getAll()
            ConsoleScreen.showSellers(sellers)

        elif menu == "4": #전체 상품 조회
            products = productDAO.getAll()
            ConsoleScreen.showProducts(products)

        elif menu == "5": #
            pageCount = sellerDAO.getPageCount("") #특정 단어 포함해서 검색안할땐 전부다 나오게
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            sellers = sellerDAO.get(pageNo, "")
            ConsoleScreen.showSellers(sellers)
        
        elif menu == "6":
            pageCount = productDAO.getPageCount("")
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            products = productDAO.get(pageNo, "")
            ConsoleScreen.showProducts(products)

        elif menu == "7": #특정 판매자 조회
            searchTxt = ConsoleScreen.showSearchMenu() 
            pageCount = sellerDAO.getPageCount(searchTxt)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            sellers = sellerDAO.get(pageNo, searchTxt)
            ConsoleScreen.showSellers(sellers)

        elif menu == "8":
            searchTxt = ConsoleScreen.showSearchMenu()
            pageCount = productDAO.getPageCount(searchTxt)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            products = productDAO.get(pageNo, searchTxt)
            ConsoleScreen.showProducts(products)

        elif menu == "9": #특정 상품 조회
            searchTxt = ConsoleScreen.showSearchMenu()
            pageCount = productDAO.getPageCount(searchTxt)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            products = productDAO.get2(pageNo, searchTxt)
            ConsoleScreen.showProducts2(products)

        elif menu == "11":
            products = productDAO.getMaxPriceProduct()
            ConsoleScreen.showProducts2(products)