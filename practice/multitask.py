def consumer():
    n = 0
    print('consumer init')
    while True:
        n = yield n
        if not n:
            return
        n -= 1
        print('消费了1, 还剩余{}'.format(n))


def produce(c):
    n = 0
    next(c)
    while n < 6:
        n += 2
        print('生产了2，总共有{}'.format(n))
        n = c.send(n)
        print('确认还剩：{}'.format(n))

    c.close()

c = consumer()
produce(c)