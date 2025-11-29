def test(a):
    print('a : ', a)
    if a == 0:
        print('끝났습니다')
    else:
        test(a - 1)

a = 7        
test(a)