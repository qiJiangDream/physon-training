#coding:utf-8

import csv   #csvモジュールをインポートする

f = open('201701/AUDJPY_20170103.csv', 'rb')
hl = []
dataReader = csv.reader(f)
header = next(dataReader)
for row in dataReader:
	print ",".join(row)
