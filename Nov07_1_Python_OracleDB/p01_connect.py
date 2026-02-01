# 지금 사용하고 있는 노트북에서 작업중인 Python 프로그램이랑
# OracleDB서버 연결
#########################################
# 컴퓨터통신은 크게 이렇게 나뉨
#   Socket: 실시간                  ex) 카톡
#   HTTP : 안실시간  이거임         ex) 인터넷브라우저
#########################################
# Python - DB 걍 둘이 통신 하는거
#   안실시간인데 HTTP통신은 아니고 걍 별개의 통신
#   DB회사 준나 다양함
#       그 다양한 DB회사들 간의 표준화된 통신방식같은게 없음;;
#       -> 그래서 DB회사별로 통신방식이 다 다름 
#       -> Python 입장에서 다 다른 통신방식을 다챙김?? => 쌉불가
#       -> Python - DB서버 연결기능은 없음 -> ㄹㅇ 만들어야함 ㅎㅎㅎㅎ
######################
# Python이 오피셜하게 만들어 준건 없음
# 근데 Python의 특징인 남이 작업해둔게 졸라 많아서 누군가 OracleDB연결 기능 만들었겠지? 그럼 그거 갖다 쓰면됨
# -> 각 DB회사에서 만들어준게 있음
#####################
# cx_Oracle.py(구버전) : cx_Oracle.py + instantclient
# oracledb.py(신버전) : instantclient 따로 없어도 되는데..
#       oracledb.py(신버전) 여기에 포함된 instantclient가 OracleDB 구버전 지원x
#       구버전 OracleDB랑 연결하려면 따로 instantclient있어야함
#########################
# pip : 개발자들간의 공유문화를 중앙제어시스템
# 시작 - cmd
#   pip install 이름 -> 다운받아와서 사용가능하게 세팅까지 완료해줌

# pip install oracledb

from oracledb import connect

# sqlplus 아이디/비번@서버주소:포트/SID
con = connect("js/1234@195.168.9.58:1521/xe") # sqlplus써서 연결할때 주소 쓰는 형식

print(con)

con.close()