from diaries.YujiDiary import YujiDiary
from diaries.YushinDiary import YushinDiary
from diaries.TomizawaDiary import TomizawaDiary
from diaries.SuzukiDiary import SuzukiDiary
from diaries.iwasakiDiary import iwasakiDiary
from diaries.TakedaDiary import TakedaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
           YushinDiary(), 
           YujiDiary(),
           TomizawaDiary(),
           SuzukiDiary(),
           iwasakiDiary(),
           TakedaDiary(),
          ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
