from diaries.AbstractDiary import AbstractDiary

class YujiDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "意図的にコンフリクトを起こすことによって、Githubの理解が深まった気がする！"

    def get_author(self):
        return "yu-ji"
