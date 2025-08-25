import boto3
import os
import re
from boto3.dynamodb.conditions import Key

def main():
    repo_name = os.environ.get("REPO_NAME")
    new_word = os.environ.get("NEW_WORD")
    region = os.environ.get("AWS_REGION", "ap-northeast-1")

    if not repo_name or not new_word:
        print("❌ REPO_NAME または NEW_WORD が未定義です")
        exit(1)

    new_word = re.sub(r'^\d+_', '', new_word)
    print(f"🔤 正規化された単語: {new_word}")

    dynamodb = boto3.resource("dynamodb", region_name=region)
    table = dynamodb.Table("pytori_shiritori")

    try:
        response = table.query(
            IndexName="repository_name-index",
            KeyConditionExpression=Key("repository_name").eq(repo_name)
        )
        items = response.get("Items", [])
        print(f"📦 取得レコード数: {len(items)}")

        if not items:
            print("🆕 新規参加リポジトリです")
            exit(0)

        sorted_items = sorted(items, key=lambda x: x.get("merged_on", ""), reverse=True)
        last_word = sorted_items[0].get("current_word", "")

        print(f"🔚 最後の単語: {last_word}")
        print(f"🆕 提出された単語: {new_word}")

        if not last_word or new_word.startswith(last_word[-1]):
            print("✅ しりとり成立！")
            exit(0)

        raise Exception(f"❌ しりとり失敗: {last_word} → {new_word}")

    except Exception as e:
        print(f"🔴 DynamoDB query failed: {e}")
        exit(1)

if __name__ == "__main__":
    main()
