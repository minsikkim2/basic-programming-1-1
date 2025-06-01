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