#coding:utf-8

import csv   #csvモジュールをインポートする
import numpy as np #npモジュールをインポートする

f = open('201701/AUDJPY_20170103.csv', 'rb')
hl = [] 
array_array =[]
dataReader = csv.reader(f)
header = next(dataReader)
cnt = 0
# 終値-始値が正->"+" / 負->"-"
# date_time[] に日時を格納する
for row in dataReader:
	
	array_temp =[]
	a = float(row[8])-float(row[5])
	if a > 0:
		array_temp.append(row[0])
		array_temp.append(cnt)
		array_temp.append("+")
		array_array.append(array_temp)
	else:
		array_temp.append(row[0])
		array_temp.append(cnt)
		array_temp.append("-")
		array_array.append(array_temp)
	cnt += 1
	
	
# from pprint import pprint
# pprint(array_array)

# print array_array[len(array_array)-2 ][0],array_array[len(array_array)-2][1],array_array[len(array_array)-2][2]
# print array_array[len(array_array)-1 ][0],array_array[len(array_array)-1][1],array_array[len(array_array)-1][2]

#indexは0から1439
#1439 = 1441(ファイル内の行数) - 1(Header除外) - 1(indexのカウント) 
# print len(array_array)-1 



# cnt = 0 #loop count 
cnts = 0 #連続した回数
cnt_row = 0 #rows num 

# for array in array_array:
# 	if cnt =0:
		
# 	else if cnt!=0:
		
# 		if array[cnt][0]==array[cnt-1][0]:
			
# 			cnts +=1
# 			if hl[cnt] == "+":
# 				temp_array =[] #
# 				temp_array.append(cnts) #result 
# 				temp_array.append(cnt_row) # 
# 				array_array.append(temp_array) #二次元配列に格納
		
# 		else:
# 			cnts =0
			
# 	cnt_row += 1	
# 	cnt +=1
	
	
# from pprint import pprint
# pprint(array_array)

# max_result = np.array(dual_array).max(0)
# print  max_result

# max_result = max_result.max(0) #０番目の要素の最大値をもつ配列を代入
# print date_time[max_result - 2]