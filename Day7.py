'''n = int(input("enter the number: "))
if n % 2 == 0:
    print(n,":짝수입니다")
else:
    print(n,":홀수입니다")
'''
n = int(input("키를 입력해 주세요: "))
k = int(input("몸무게를 입력해 주세요 : "))
BMI = k/ n**2
if  18.5 <= BMI <= 22.9:
    print(f"BMI는 {BMI:.i}이며,정상입니다")
else:
    print(f"BMI는 {BMI:.i}이며,비정상입니다")