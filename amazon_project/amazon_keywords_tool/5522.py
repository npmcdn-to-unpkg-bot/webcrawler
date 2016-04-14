import time
try:
	with open('keywords.txt') as k, open('brandsfile.txt') as b:
		keywords = k.read().split()     #转化为单个单词的list
		diff_keywords=list(set(keywords))       #通过set去重后转回list
		diff_keywords.sort(key=keywords.index)  #保持原顺序
		#print(diff_keywords)

		brands=list(set(b.read().split()))
		final_keywords=[word for word in diff_keywords if word not in brands]
		#print(final_keywords)
		
		
except IOError as err:
	print("File error: ", str(err))


length = 0
j = 0
k = 0
target_dir = time.strftime('%Y%m%d%H%M%S') + '.txt'
try:
	with open(target_dir ,'w') as target:
		for i in final_keywords:
			if j < 5:
				if length + len(i) + 1 < 50:
					target.write(i+' ')
					length = length + len(i) + 1
				else:
					target.write('\n\n')
					target.write(i+' ')
					length = len(i)
					j += 1
			elif k < 2:
				if length + len(i) + 1 < 2000:
					target.write(i+' ')
					length = length + len(i) + 1
				else:
					target.write('\n\n')
					length = 0
					k += 1
			else:
				j = 0
				k = 0
			
except IOError as err:
	print("File error: ", str(err))
