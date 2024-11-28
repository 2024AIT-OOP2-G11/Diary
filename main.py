from diaries.YujiDiary import YujiDiary
from diaries.YushinDiary import YushinDiary
from diaries.TomizawaDiary import TomizawaDiary
from diaries.SuzukiDiary import SuzukiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
           YushinDiary(), 
           YujiDiary(),
           TomizawaDiary(),
           SuzukiDiary(),
          ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
