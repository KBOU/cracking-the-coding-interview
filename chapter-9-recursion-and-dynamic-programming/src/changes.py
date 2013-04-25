# coding: utf-8

def changes(cents, coin_type=25):
    if coin_type == 25:
        smaller_coin_type = 10
    elif coin_type == 10:
        smaller_coin_type = 5
    elif coin_type == 5:
        smaller_coin_type = 1
    elif coin_type == 1:
        return 1

    ways = 0
    for i in range(0, cents+1, coin_type): 
        ways += changes(cents - i, smaller_coin_type)
    return ways

if __name__ == "__main__":
    print changes(100)
