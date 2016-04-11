with open('adwords.txt') as file, open('result.txt', 'w') as target, open('brandsfile.txt') as brand:
    brands = [b.strip() for b in brand.readlines()]
    # print(brands)
    data = file.readlines()
    new_data = list(set(data))
    word_list = []
    for i in new_data:
        j = i.split()
        word_list.extend(j)
    new_words = list(set(word_list))
    new_words.sort(key=word_list.index)
    length = 0
    # print(word_list)
    # print(new_words)
    for k in new_words:
        if length + len(k) < 1000:
            if k not in brands:
                target.write(k+' ')
                length += len(k)+1




