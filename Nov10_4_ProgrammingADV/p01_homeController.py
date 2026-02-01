# PM, 사수가 하는 부분탈모
from p01_companyDAO import CompanyDAO
from p01_consoleScreen import ConsoleScreen

if __name__ == "__main__":
    c = ConsoleScreen.getInfo()
    result = CompanyDAO.reg(c)
    ConsoleScreen.printResult(result)

