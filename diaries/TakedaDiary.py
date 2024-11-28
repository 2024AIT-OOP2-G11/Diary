from diaries.AbstractDiary import AbstractDiary

class TakedaDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "今日は急遽バイトが入った"

    def get_author(self):
        return "Sample"
