n = int(input("숫자를 입력하세요:"))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print(f"{n}! =",fact) #f_string 을 사용하여 n의 값이 문자열 안에 들어가서 출력되게 함