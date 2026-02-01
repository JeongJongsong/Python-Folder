from p02_doctor import Doctor
from p02_consoleScreen import ConsoleScreen
# 여기서는 
if __name__ == "__main__":
    g = ConsoleScreen.getGuestInfo()
    Doctor.calculate(g)
    ConsoleScreen.printResult(g)