class jeongStringCleaner:
    @staticmethod
    def clean(txt):
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        return txt
    
# <b></b>처리하는게 네이버뿐만 아니라 카카오 ...등등
#   지금처리 -> 처리하는거 나중에도 필요할듯 -> 회사가서도
#   -> 처리하기 편하게 정리를 해보자 

# library vs framework  
#   library
#       자주 쓸것같은 기능을 아에 따로 정리해놓음
#       파일(패키지) 통째로 갖고 다니면서
#       필요할때마다 쓰기 편하게
#   framwork :
#       library + 자체개발툴
#   framwork > library 근데 구별 잘 안함