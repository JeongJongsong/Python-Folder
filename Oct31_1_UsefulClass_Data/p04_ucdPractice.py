# 카톡 톡방 아무거나 하나 대화내용 가져와보기
# 대화 내용만 -> 시간 지워야하는데 어캐지우지??
# 단어수 세기
#  무슨 단어 제일 많이 썻나 

# 시간 어캐 지우지??? 
# ->객체로 만들어서 그것만 입력시키면 대화만 나오지 않을까?
# -> 아니면 split으로 나누고 하면 ???
# 그럼 split으로 나눈 대화부분에도 " : " 있음 어칼꺼?
# 대화내용이 길어져서 다음줄로 간경우 " : " 이 없데 어캄??
# 대화내용 줄에 " : " 없고 공백있음 어칼꺼?

# 내 지금 상황 -> 영어 배우고 있다는 상황이라 치고
# 닭을 영어로 뭐라하냐 -> 치킨이라고 할것 같아요 ->그럼 써봐 -> 쓰는걸 못함
# 어캐 하면 될것 같다 까지 생각이 들긴함 but 그걸 못씀
 
from dataclasses import asdict


f = open("C:\\Users/soldesk/Desktop/kakao/KakaoTalkChats.txt", "r", encoding= "utf-8")
wordcount = {}
for i, line in enumerate(f.readlines()):
    if line.startswith("2019"):
        break
    msg = None
    if i > 4: #받아온 대화파일에 첫 5줄은 필요없는부분이라 없앰
        line = line.replace("\n", "")
        
        if (not line.startswith("20")) and (line !=""):
            print(line) #->10번줄 내용을 프린트한거
            msg = line
        else:
            try:
                line = line.split(" : ")
                msg = line[1]
                for ii, word in enumerate(line):
                    if ii > 1:
                        msg += " " + word
            except:
                pass
        if msg != None:
            msg = msg.strip().split(" ")
            for word in msg:
                if word in wordcount:
                    wordcount[word] += 1
                else:
                    wordcount[word] = 1
f.close()
print(wordcount)


# 3/5/2 중에 5임 못푸는게 당연한거고
# 이 문제를 어떻게 풀어야할까?? 생각이라도 해보라고 낸 문제임
# 배운것들 토대로 어캐 해볼지 생각했으면 그걸로 된거임.
# 해결하라고 낸 문제 아니다 못하는게 당연한거다 이자시가