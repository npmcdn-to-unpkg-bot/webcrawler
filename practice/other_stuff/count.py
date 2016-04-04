a = ['asd', 'bbb', 'ewrewr','re','nbn']

b = [i for i in a if 're' != i]

c = [i for i in a if 're' not in i]

print(b)

print(c)