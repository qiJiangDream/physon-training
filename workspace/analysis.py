#coding:utf-8

import csv   #csvモジュールをインポートする

f = open('201701/AUDJPY_20170103.csv', 'rb')
# hl = []
dataReader = csv.reader(f)
# header = next(dataReader)
cnt = 0
for row in dataReader:
	cnt += 1
	print cnt
