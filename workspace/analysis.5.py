#coding:utf-8

import csv   #csvモジュールをインポートする
import numpy as np #npモジュールをインポートする

f = open('201701/AUDJPY_20170103.csv', 'rb')
dataReader = csv.reader(f)
header = next(dataReader)
array_array =[] #二次元配列の変数名
cnt = 0 #カウント変数

for row in dataReader:
	array_temp =[] #tmpの配列変数
	a = float(row[8])-float(row[5])
	if a > 0:
		#tmpの配列に代入する
		array_temp.append(row[0])
		array_temp.append(cnt)
		array_temp.append("+")
		# 二次元配列に代入する
		array_array.append(array_temp)
	else:
		#tempの配列に代入する
		array_temp.append(row[0])
		array_temp.append(cnt)
		array_temp.append("-")
		# 二次元配列に代入する
		array_array.append(array_temp)
		
	cnt += 1

cnts = 0		#count用の変数
cnt_result = 0  #カウンタ変数： + or - が続いた時の連続回数
dual_array = [] #二次元配列
max_cnts = 0	#最大連続回数
index = 0		#index num

# 多次元配列から配列を取り出す
for array_temp in array_array:
	
	#1行目は0行目と比較不可のため0として処理 
	if cnts == 0:
		array_temp.append(0)
		
	#2行目以降の処理
	else:
		
		# 連続回数が増加する場合
		if array_array[cnts][2]==array_array[cnts-1][2]:
			cnt_result += 1
			array_temp.append(cnt_result)
			
			# "+" かつ 最大連続回数の場合
			# その最大連続回数とindexを代入する。
			if array_array[cnts][2] == "+" and max_cnts < cnt_result:
				max_cnts = cnt_result
				index = array_array[cnts][1]
		
		# 連続回数がリセットする場合		
		else:
			cnt_result =0
			array_temp.append(cnt_result)
	
	# 連続回数を多次元配列に格納する
	dual_array.append(array_temp)		
	cnts +=1		

# 最大連続回数(10回)繰り返す
for var in range(0 , max_cnts):
	print dual_array[index-max_cnts][0],dual_array[index-max_cnts][1],dual_array[index-max_cnts][3]
	max_cnts -= 1

# 配列の中身確認用のコード
# from pprint import pprint 
# pprint(dual_array) 
	