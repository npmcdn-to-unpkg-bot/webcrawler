
with open('brandsfile.txt') as brand:
    brands = [b.strip() for b in brand.readlines()]
    # print(brands)


def get_keywords(src):
    target = []

    new_data = list(set(src))
    word_list = []
    for i in new_data:
        j = i.split()
        word_list.extend(j)
    new_words = list(set(word_list))
    print('new words before sort '+str(new_words))
    new_words.sort(key=word_list.index)
    # print('new words after sort '+str(new_words))
    length = 0
    # print(word_list)
    # print(new_words)
    for k in new_words:
        if length + len(k) < 1000:
            if k not in brands:
                target.append(k+' ')
                length += len(k)+1
    return target


def get_longtail_keywords(src):
    target = []

    new_data = list(set(src))
    for i in new_data:
        for j in i.strip().split():
            if j in brands:
                new_data.remove(i)
                break
    length = 0
    for k in new_data:
        k = k.strip()
        if length + len(k) < 1000:
            target.append(k+',')
            length += len(k) + 1
    return target

# get_keywords('adwords.txt')
if __name__ == '__main__':
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    with open('adwords.txt') as file, open('result.txt', 'w') as rt:
        data = file.readlines()
        # get_keywords(data)
        if '\n' in data:
            data1 = data[:data.index('\n')]
            data = data[data.index('\n')+1:]
            print('data1:'+str(data1))
            if '\n' in data:
                data2 = data[:data.index('\n')]
                data = data[data.index('\n')+1:]
                print('data2:'+str(data2))
                if '\n' in data:
                    data3 = data[:data.index('\n')]
                    data = data[data.index('\n')+1:]
                    print('data3:'+str(data3))
                    if '\n' in data:
                        data4 = data[:data.index('\n')]
                        print('data4:'+str(data4))
                        data5 = data[data.index('\n')+1:]
                        print('data5:'+str(data5))

        if data1:
            for i in get_keywords(data1):
                rt.write(i)
            # print('data1 in main:'+str(data1))
            print(get_keywords(data1))
        if data2:
            rt.write('\n\n')
            for i in get_keywords(data2):
                rt.write(i)
            # print('data2 in main:'+str(data2))
            print(get_keywords(data2))
        if data3:
            rt.write('\n\n')
            for i in get_keywords(data3):
                rt.write(i)
            print(get_keywords(data3))
        if data4:
            rt.write('\n\n')
            for i in get_keywords(data4):
                rt.write(i)
            print(get_keywords(data4))
        if data5:
            rt.write('\n\n')
            for i in get_longtail_keywords(data5):
                rt.write(i)
            print(get_longtail_keywords(data5))

    # print(get_keywords(data1))
    # print(get_keywords(data2))
    # print(get_keywords(data3))
    # print(get_keywords(data4))
    # print(get_longtail_keywords(data5))