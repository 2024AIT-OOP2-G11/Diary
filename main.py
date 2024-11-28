from diaries.DiarySample import DiarySample
from diaries.YujiDiary import YujiDiary
from diaries.YushinDiary import YushinDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
           YushinDiary(), 
           YujiDiary(),
          ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
