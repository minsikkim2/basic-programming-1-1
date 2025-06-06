#7
nums = input("정수 여러개를 입력하세요:").split()
num_list = [int(ch) for ch in nums]

# 최대값, 최소값 초기화
max_val = num_list[0]
min_val = num_list[0]

# 반복문을 통해 최대/최소값 찾기
for num in num_list:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(f"최대값은 {max_val}, 최소값은 {min_val}입니다.")
'''
'''
#8
num = input("입력: ")

# 문자열 인덱싱을 이용해 뒤집기
reversed_num = num[::-1]

print("출력:", reversed_num)
'''
'''
#9
n = int(input("숫자 n을 입력하세요: "))

for i in range(1, n + 1):
    print('*' * (2 * i - 1))
'''
import random

answer = random.randint(1, 100)
print("컴퓨터: 랜덤 숫자 생성 완료!")

while True:
    guess = int(input("입력: "))
    if guess > answer:
        print("더 작은 수를 입력하세요.")
    elif guess < answer:
        print("더 큰 수를 입력하세요.")
    else:
        print(f"정답입니다! ({answer})")
        break
