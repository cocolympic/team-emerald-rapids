import xml.etree.ElementTree as ET

xml_data = '''
<library>
    <book>
        <title>Python入門</title>
        <author>山田太郎</author>
        <year>2021</year>
    </book>
    <book>
        <title>AIの基礎</title>
        <author>佐藤花子</author>
        <year>2023</year>
    </book>
</library>
'''

root = ET.XML(xml_data)

for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    print(f'タイトル: {title}, 著者: {author}, 年: {year}')
# 出力例:
# タイトル: Python入門, 著者: 山田太郎, 年: 2021
# タイトル: AIの基礎, 著者: 佐藤花子, 年: 2023