# with文の例 - ファイルの読み込みとエラーハンドリング
try:
    with open("README.md", "r") as f:
        content = f.read()
        print("ファイルの内容:")
        print(content[:100] + "..." if len(content) > 100 else content)
except FileNotFoundError:
    print("ファイルが見つかりません")
except Exception as e:
    print(f"エラーが発生しました: {e}")
