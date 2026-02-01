class jeongStringCleaner:
    @staticmethod
    def clean(txt):
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        return txt