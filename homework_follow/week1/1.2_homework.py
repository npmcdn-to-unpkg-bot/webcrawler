from bs4 import BeautifulSoup

with open('1_2answer_of_homework/1_2_homework_required\index.html', 'r') as data:
    result = []
    soup = BeautifulSoup(data, 'lxml')
    title = soup.select('h4 > a')
    price = soup.select('h4.pull-right ')
    image = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    review = soup.select('div.ratings > p.pull-right')
    stars = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    print(stars)

    for title, price, image, review, stars in zip(title, price, image, review, stars):
        data = {
            'title': title.get_text(),
            'price': price.get_text(),
            'image': image.get('src'),
            'review': review.get_text(),
            'stars': len(stars.find_all('span', class_='glyphicon glyphicon-star'))
        }

        result.append(data)
    for i in result:
        if i['stars'] > 4:
            print(i)

