from diaries.DiarySample import DiarySample
from diaries.YujiDiary import YujiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           YujiDiary(),] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
