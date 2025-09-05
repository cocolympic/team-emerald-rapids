filename = "report.xlsx"
if filename.endswith((".py", ".xlsx", ".csv")):
    print("許可されたファイル形式です。")
else:
    print("許可されていないファイル形式です。")