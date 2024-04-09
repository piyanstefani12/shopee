import shopee

with open('data.txt', 'r') as cvs:
    for i in cvs.readlines():
        shopee.Shopee(nope=i)