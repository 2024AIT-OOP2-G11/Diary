from diaries.iwasakiDiary import iwasakiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [iwasakiDiary()] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
