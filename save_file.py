#小文件存储方案
#直接转换为二进制格式插入到数据库

from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.image
myset = db.mp3

# f = open('11.mp3','rb')

# content = bson.binary.Binary(f.read())

# #插入文档
# myset.insert({'filename':'11.mp3','data':content})

#提取图片
img = myset.find_one({'filename':'11.mp3'})

#将内容写入本地
with open('11.mp3','wb') as f:
    f.write(img['data'])



conn.close()
