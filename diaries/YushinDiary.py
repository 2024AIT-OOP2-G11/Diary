from diaries.AbstractDiary import AbstractDiary

class YushinDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "マックの充電器を忘れた。貸してくれてありがと！"

    def get_author(self):
        return "yu-shin"
