from splinter import Browser
import time
seed=open('seed.txt')
myseed=seed.readlines()
seed.close()

b=open('brandsfile.txt')
brands=list(set(b.read().split()))
b.close()

b=Browser('chrome')
b.visit('http://fanzle.com/amazon-longtail-keyword-scraper')
b.find_by_value('3').click()
b.find_by_tag('textarea').fill(myseed)
b.find_by_value('submit').click()
search=True
while search:
    time.sleep(2)
    if int(b.find_by_id('current').value)==int(b.find_by_id('total').value):
        search=False
keywords=b.find_by_tag('tbody').value.split()
diff_keywords=list(set(keywords))
diff_keywords.sort(key=keywords.index)
diff_keywords.pop(0)
final_keywords=[word for word in diff_keywords if word not in brands]

fw=open('fazleword.txt', 'w')
for i in final_keywords:
	fw.write(i+' ')
fw.close()

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


time.sleep(1)
win = b.windows[0]
win.close()
