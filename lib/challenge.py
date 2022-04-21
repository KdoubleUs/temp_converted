nums=101


def tryFizz(x): 
    for x in range(0,100):
        if x%3==0: 
            print('divisble by 3 FIZZ')
        elif x%5==0: 
            print('divisible by 5 BUZZ')
        elif x%3==0 and x%5==0: 
            print('divisible by both 3 and 5 FIZZBUZZ')
        else: 
            print(x)

tryFizz(100)