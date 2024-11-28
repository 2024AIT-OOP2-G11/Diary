from diaries.AbstractDiary import AbstractDiary

class TomizawaDiary(AbstractDiary):
    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
        return """おなかすいた"""

    def get_author(self):
        return "Tomizawa"