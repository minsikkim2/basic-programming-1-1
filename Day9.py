#3
n = int(input("숫자를 입력하세요:"))
for i in range(1,10):
    m = n*i
    print(f"{n}x{i}={m}")
'''
'''
#4
n= int(input("숫자를 입력하세요:"))
nsum = 0
for i in range(1,n+1):
    nsum = nsum + i
print(f"입력:{n}\n출력:{nsum}")
'''
'''
#5
n= int(input("숫자를 입략하세요:"))
nfact =1
for i in range(1,n+1):
    nfact = nfact*i
print(f"{n}!={nfact}")
'''

nums = input("정수 여러개를 입력하세요:").split() #space로 구분
nums =list(map(int, nums))
total = 0
for i in nums:
    total = total + i
average = total/len(nums)
print("입력한 정수의 리스트:",nums)
print(f"평균은{average}입니다.")