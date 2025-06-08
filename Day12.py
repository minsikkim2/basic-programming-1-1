# ch5
# 2차원 그래프
'''
import matplotlib.pyplot as plt  # matplot 라이브러리를 터미널을 이용해 다운로드
x = [1,2,3,4,5,6,7]
y = [1,2,3,4,5,6,7]
plt.plot(x, y) #매트랩과는 달리 앞에 plt.을 붙여야함 -matplotlib의 pyplot을 plt라는 이름으로 import한다는 뜻
plt.title('선 그래프 예제')
plt.xlabel('X축')
plt.ylabel('Y축')
plt.show()
'''

# hold
'''
import numpy as np #np 라는 이름으로 numpy 를 import한다는 뜻
import matplotlib.pyplot as plt

x1 = np.arange(-2, 4, 0.3) #np.arange 는 matlab에서 : 과 같은 효과
y1 = 3.5 ** (-0.5 * x1) * np.cos(6 * x1) # **는 matlab에서 ^:거듭제곱)
plt.plot (x1,y1)

x2 = np.arange(-2, 4, 0.01)
y2 = 3.5 ** (-0.5 * x2) * np.cos(6* x2) 
plt.plot (x2,y2) #plot을 2번 써주면 matlab에서 hold를 한것과 같다

plt.show()
'''
# fplt
'''
import numpy as np
import matplotlib.pyplot as plt

def f(x): #def 를 이용하여 함수 정의
    return x**2
x = np.arange(0.0, 10, 0.5)
y = f(x)

plt.plot(x,y)
plt.show()
'''
# bar graph
'''
import numpy as np
import matplotlib.pyplot as plt

year = np.arange(1988,1995,1) #배열에서 마지막 값은 포함을 안하기 때문에 1995 로 해야 크기가 맞음
sale=[8, 12, 20, 22, 18, 24, 27]

plt.bar(year, sale, color = 'red') #매트랩과 달리 색을 color = '' 으로 정의해줘야 함
plt.title('bar graph')
plt.xlabel('Year')
plt.ylabel('Sales (Millions)')
plt.show()
'''
# barh
'''
import numpy as np
import matplotlib.pyplot as plt

year = np.arange(1988,1995,1) #배열에서 마지막 값은 포함을 안하기 때문에 1995 로 해야 크기가 맞음
sale=[8, 12, 20, 22, 18, 24, 27]

plt.barh(year, sale, color = 'red')  #매트랩과 같이 barh 는 가로막대 그래프를 나타냄
plt.title('bar graph')
plt.xlabel('Year')
plt.ylabel('Sales (Millions)')
plt.show()
'''
# stem graph
'''
import numpy as np
import matplotlib.pyplot as plt

year = np.arange(1988,1995,1) 
sale=[8, 12, 20, 22, 18, 24, 27]

plt.stem(year,sale)
plt.title('stem graph')
plt.xlabel('Year')
plt.ylabel('Sales (Millions)')
plt.show()
'''
# pie graph
'''
import matplotlib.pyplot as plt

grd = [11, 18, 26, 9, 5]
plt.pie(grd, autopct='%1.f%%') #배열의 값들을 퍼센트로 계산(소수점 첫째자리까지)
plt.show()
'''
# ch6
# if-else
'''
h = 50
t = 50

if t <40:
    pay = h * t
else:
    pay = h * 40 + (t - 40) * h * 1.5

print(f"The worker's pay is {pay:.2f}") #소수점 둘쨰 자리까지 포맷

'''
# for-end
'''
for i in range(10): #range를 이용
    print("hello!")

'''
'''
for i in range(10):
    i = i + 1
    print(i)
'''
'''
n = int(input("input the number:"))
for i in range(1, n+1): # range로 시작과 끝을 결정할 수 있음 위 예제처럼 i에 1을 더할 필요 없음
    print(i, end =' ') # end =''를 이용하여 한줄에 숫자를 나타낼 수 잇음 '' 안에 스페이스 수만큼 공백 생김
'''
'''
n = int(input("input the number:"))
for i in range(1, n+1,2): # 간격 설정 가능
    print(i) 
'''
'''
n = 100
sum = 0
for i in range(1,n+1):
    sum = sum + i
    print(sum)
'''
'''
n = 100
sum = 0
for i in range(1,n+1):
    sum = sum + i*(i+1)

print(sum) #위의 예제와 달리 print를 for문 바깥으로 옮기면 계산과정 없이 최종결과만 출력
'''
'''
n = int(input("숫자를 입력하세요:"))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print(f"{n}! =",fact) #f_string 을 사용하여 n의 값이 문자열 안에 들어가서 출력되게 함
'''
'''
n = 100
nsum = 0.0
def ak(k):
    return 4* (-1)**(k-1) / (2*k -1)
for k in range(1, n+1):
    nsum = nsum + ak(k)

print("sum(from 1 to n) =", nsum)
'''
'''
a = 12-4
b = 5*3
print(a<b)
'''
# problem 6
'''
rows = 3
cols = 5
matrix = [] #행렬을 저장할 빈 리스트를 만듬

for i in range(1, rows +1):
    row = [] #행의 원소들을 저장할 리스트 생성
    for j in range(1, cols +1):
        value = (i**j)/(i+j)
        row.append(value) #행에 값 추가
    matrix.append(row) 
for row in matrix:
    print(row)
'''
# problem7
'''
import math

n = 5  # 행렬의 크기 (n x n)
A = []  # 파스칼 대칭행렬을 저장할 리스트

for irow in range(1, n + 1):  # 1부터 n까지 (행)
    row = []
    for jcol in range(1, n + 1):  # 1부터 n까지 (열)
        value = math.factorial(irow + jcol - 2) // (math.factorial(irow - 1) * math.factorial(jcol - 1))
        row.append(value)
    A.append(row)

for row in A:
    print(row)
'''
# problem8
'''
import numpy as np

# 데이터 입력
BOS = [2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93]
SEA = [6.83, 3.63, 7.20, 2.68, 2.05, 2.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.85]

# (a) 도시별 한 해 총 강수량과 월 평균 강수량 계산
BOS_total = sum(BOS)
SEA_total = sum(SEA)
BOS_mean = np.mean(BOS)
SEA_mean = np.mean(SEA)

print(f"(a) Boston의 2012년 총 강수량: {BOS_total:.2f}")
print(f"(a) Seattle의 2012년 총 강수량: {SEA_total:.2f}")
print(f"(a) Boston의 월 평균 강수량: {BOS_mean:.2f}")
print(f"(a) Seattle의 월 평균 강수량: {SEA_mean:.2f}")

# (b) 도시별 평균 강수량보다 많은 강수량을 보인 달의 개수
BOS_above_mean_months = [i+1 for i, val in enumerate(BOS) if val > BOS_mean]
SEA_above_mean_months = [i+1 for i, val in enumerate(SEA) if val > SEA_mean]

print(f"(b) Boston 평균보다 강수량이 많은 달: {len(BOS_above_mean_months)}개월 ({BOS_above_mean_months})")
print(f"(b) Seattle 평균보다 강수량이 많은 달: {len(SEA_above_mean_months)}개월 ({SEA_above_mean_months})")

# (c) 시애틀의 강수량보다 보스턴의 강수량이 더 적은 달의 개수 및 월
BOS_less_than_SEA_months = [i+1 for i, (b, s) in enumerate(zip(BOS, SEA)) if b < s]

print(f"(c) 보스턴의 강수량이 시애틀보다 적은 달: {len(BOS_less_than_SEA_months)}개월 ({BOS_less_than_SEA_months})")
'''
# problem 9
'''
import math

k = 0
s = 0
while s <= 120:
    k += 1
    if k % 13 == 0 and k % 16 == 0:
        s = math.sqrt(k)
print(f"요구 조건을 만족하는 수는:{k}")
'''
# problem10
'''
n = 20
a = [1, 1]

for k in range(2, n):
    a.append(a[k-1] + a[k-2])

print(a)
print(a[-1])     
'''
# problem 19
for a in range(1, 51):
    for b in range(1, 51):
        for c in range(1, 51):
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
