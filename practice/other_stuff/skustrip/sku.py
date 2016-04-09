import csv

with open('skustrip.csv') as data:
    reader = csv.reader(data)
    file = list(reader)
    sku1 = []
    sku2 = []
    for i in file:
        sku1.append(i[0])
    # print(sku1)
    for j in file:
        sku2.append(j[1])

    sku3 = set(sku1) - set(sku2)
    result = list(sku3)
    with open('output.txt', 'w') as out:
        for k in result:
            out.writelines(k+'\n')