# analysisSubway
# 요일별 이용객수 (탄+내린)평균
# -> 무슨요일 이용객수 가장 많은가

# 데이터분석

# 1) 파일 전체말고 부분부분만 출력
# 2) 요일구하기, 탄사람, 내린사람 콘솔출력
# 3) 
# 탄수 + 내린수 각각 객체로 만들어서 더해서 평균

from datetime import datetime


f = open("C:/Users/soldesk/Desktop/Jeongjs/subway.csv", "r", encoding="utf-8")
subwaySum = {"Sun":0, "Mon":0, "Tue":0, "Wed":0, "Thu":0, "Fri":0, "Sat":0}
subwayCnt = {"Sun":0, "Mon":0, "Tue":0, "Wed":0, "Thu":0, "Fri":0, "Sat":0}
for line in f.readlines():     
    line = line.replace("\n", "").split(",")
    when = "%s,%s,%s" % (line[0],line[1],line[2])
    when = datetime.strptime(when, "%Y,%m,%d")
    yoil = datetime.strftime(when, "%a")
    sum = int(line[5]) + int(line[6])
    subwaySum[yoil] += sum
    subwayCnt[yoil] += 1
f.close()

for k, v in subwaySum.items():
    print(k, (v / subwayCnt[k]))
# 요일별 합계       Sun : 123124, Mon :54235 .....
# 요일별 데이터수   Sun : 434   , Mon : 53 .....  -> dict 로
# 요일별 평균       Sun : 1544.1, Mon : 15423.2 .....