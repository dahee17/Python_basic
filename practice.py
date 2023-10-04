# 문제 1) 입력된 단수를 출력하는 코드
# dan = int(input("단수")
# for i in range(1, 10):
#   print(f"{dan}x{i}={dan*i}")

# 문제 2) 2단~ 9단까지 출력하기(2~9) => 해당 단 출력, 중첩 for 문
# 구구단 2단 출력
# 2x1=2
# 2x2=4
# ...
# 2x9=18
for i in range(2, 10):
    for j in range(1,10):
        print(f"{i}x{j}={i*j}")

# 문제 3) list a의 평균값을 계산하세요.
print("=" * 200)
a = {1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4}
total = 0
for i in a:
    total += i
length = len(a)
result = total / length
# round(값, 소수점숫자) : 반올림
print(round(result,2)) # 평균값

# 문제 4) list b에서 최소값 찾기!
b = [22, 1, 4, 7, 98]

print(num_min)  # 1 출력
