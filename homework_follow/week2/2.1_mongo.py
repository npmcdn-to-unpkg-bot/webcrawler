import pymongo

client = pymongo.MongoClient('localhost', 27017)
walden = client['walden']
tab_lines = walden['tab_line']

# with open('Walden.txt', encoding='utf-8') as f:
#     lines = f.readlines()
#     for index, line in enumerate(lines):
#         data = {
#             'index': index,
#             'line': line,
#             'words': len(line.split())
#         }
#         print(data)
#         tab_lines.insert_one(data)


# for item in tab_lines.find({'words': {'$lt': 100, '$gt': 90}}):
#     print(item)

print(tab_lines.find().count())