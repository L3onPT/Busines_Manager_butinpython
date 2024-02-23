from time import sleep

money = 100000

while 1 == 1:
    sleep(1)
    if money >= 1000000:
        money = money / 1000000
        print(money, "M$")
    
    elif money >= 1000:
        money = money / 1000
        print(money, "K$")
    
    print(money, "$")