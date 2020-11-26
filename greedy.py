# from random import *

# # -- 거스름돈 문제 --

# n = randint(1, 1000) * 10
# count = 0
# coin_array = [500, 100, 50, 10]

# print(n)

# # 큰 단위의 화폐부터 차례대로 확인하기

# for coin in coin_array:
#     count += n // coin
#     n %= coin

# print(count)

# # ----------------------

# -- 그리디 나누기 문제 --
# N, K 를 공백을 기준으로 구분하여 입력 받기
# n, k = map(int(input().split())
# 또는
n = int(input())
k = int(input())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

# ------------------------
