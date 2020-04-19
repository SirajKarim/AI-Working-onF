from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LTTextBoxHorizontal
import os
import json
import PyPDF2
import pymongo
from pymongo import MongoClient


fp = open('- Team KIET Stars - Alejandro Cremades - The Art of Startup Fundraising - Pitching Investors, Negotiating the Deal, and Everything Else Entrepreneurs Need to Know (2016).pdf', 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)
# Get the outlines of the document.
outlines = document.get_outlines()
# data = []
# dic = {}
count = 0
myd = {}
for (level,title,dest,a,se) in outlines:
      print (level, title)
      myd = {}
      myd["level"] = title
      print(myd)
      client = MongoClient()
      client = MongoClient('localhost',27017)
      db = client.dammyDatabase
      collection = db['forum']
      collection.insert_one(myd)
      # client = MongoClient()
      # client = MongoClient('localhost',27017)
      # db = client.dammyDatabase
      # collection = db['forum']
      # collection.insert_one({"Level":level"Title":title})

      # dic.append({"level",level,"title",title})
      # data.append({"level",level,"title",title})
      # print (level, title)

# print(dic)
# print(data)
# gldic = {}
# for i in data:
#    gldic[i] = data[0]
   
   
# print(len(data))
# # for i in data:
# #       print(i)
# print(data[1])

# json_path = 'w9.json'
# with open(json_path, 'a') as fh:
#         json.dump(data, fh)


# client = MongoClient()
# client = MongoClient('localhost',27017)
# db = client.dammyDatabase
# collection = db['forum']
# for i in data:
#       collection.insert_one(i)

# print("done")



# myFile = open('test.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(myFile)
# pg=pdf_reader.getPage(8)
# ff = pg.extractText()
# counter = 1
# data = {}
# data['Pages'] = []
# page = {'Page_{}'.format(counter): ff}
# data['Pages'].append(page)
# json_path = 'w9.json'
# with open(json_path, 'w') as fh:
#         json.dump(data, fh)
# print(ff)


# print('.....done')

# import string
# dictionaries = {}  # dicts
# count = 0
# for name in ["lloyd", "alice", "tyler"]:
#     dictionaries[name]={"homework": [], 
#         "quizzes": [], "tests": []}

# print(dictionaries)