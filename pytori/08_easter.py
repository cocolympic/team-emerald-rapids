from dateutil.easter import easter

year = 2023
for i in range(5):
    easter_date = format(easter(year), "%m月%d日")
    print(f"{year}年 のイースターは {easter_date} です")
    year += 1