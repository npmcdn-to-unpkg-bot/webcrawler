from splinter import Browser
import time

myseed = []
try:
	with open('seed.txt') as seed:
		myseed = seed.readlines()
except IOError as err:
	print("File error: ", str(err))

browser1 = Browser('chrome')
browser1.visit('http://app.scientificseller.com/keywordtool')
#browser1.reload()
browser1.find_by_tag('textarea').fill(myseed)
browser1.find_by_tag('button').click()
browser1.find_by_tag('input').fill('fafafa')
browser1.find_by_tag('button').click()

volume = 0
try:
	with open('volume.txt') as v:
		vol = v.readlines()
		volume = vol.pop()
#		print(volume)
except IOError as err:
	print('File error: ',str(err))

loop = True
while loop:
#	print(browser1.find_by_tag('strong').value + '\n')
	time.sleep(5)    
	if int(browser1.find_by_tag('strong').value) > int(volume):
		loop = False
browser1.find_by_tag('button').click()

time.sleep(5)	# Wait for html code coming into being

content = browser1.find_by_tag('td').value

keywords = content.split()
diff_keywords = []
for i in keywords:
	if diff_keywords.count(i) == 0:
		diff_keywords.append(i)

diff_keywords.pop(0)
diff_keywords.pop(0)
diff_keywords.pop(0)

# print(diff_keywords)

brands=[]
try:
	with open('brandsfile.txt') as b:
		for each_line in b:
			each_line = each_line.strip()
			brands.append(each_line)
except IOError as e:
	print("File error: ", str(e))

no_brands_keywords = [k for k in diff_keywords if k not in brands]

deleted_words = [d for d in diff_keywords if d in brands]
try:	
	with open('deleted.txt', 'w') as deleted:
		
		for i in deleted_words:

			deleted.write(i+' ')
except IOError as err:
	print("File error: ",str(err))
# print(no_brands_keywords)

length = 0
j = 0
k = 0
target_dir = time.strftime('%Y%m%d%H%M%S') + '.txt'
try:
	with open(target_dir ,'w') as target:
		for i in no_brands_keywords:
			if j < 5:
				if length + len(i) + 1 < 50:
					target.write(i+' ')
					length = length + len(i) + 1
				else:
					target.write('\n\n')
					target.write(i+' ')
					length = len(i)
					j += 1
			elif k < 1:
				if length + len(i) + 1 < 1000:
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

time.sleep(1)
win = browser1.windows[0]
win.close()
