#coding:utf-8

import csv   #csvモジュールをインポートする

f = open('201701/AUDJPY_20170103.csv', 'rb')
hl = []
dataReader = csv.reader(f)
header = next(dataReader)
for row in dataReader:
	a = float(row[8])-float(row[5])
	if a > 0:
		hl.append("+")
	else:
		hl.append("-")



cnt = 0
cnts = 0
for x in hl:
	cnt += 1
	print x , cnt
	# if cnt!=0:
	# 	if hl[cnt]==hl[cnt-1]:
	# 		cnts +=1
	# 	else:
	# 		cnts =0
	# 	print cnts
	# cnt +=1
	
	