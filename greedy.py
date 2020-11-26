# -- 거스름돈 문제 --

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
coin_array = [500, 100, 50, 10]

for coin in coin_array:
    count += n // coin
    n %= coin

print(count)

# ----------------------
