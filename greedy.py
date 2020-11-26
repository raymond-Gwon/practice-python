from random import *

# -- 거스름돈 문제 --

n = randint(1, 1000) * 10
count = 0
coin_array = [500, 100, 50, 10]

print(n)

# 큰 단위의 화폐부터 차례대로 확인하기

for coin in coin_array:
    count += n // coin
    n %= coin

print(count)

# ----------------------
