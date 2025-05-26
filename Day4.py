h = 50
t = 50

if t <40:
    pay = h * t
else:
    pay = h * 40 + (t - 40) * h * 1.5

print(f"The worker's pay is {pay:.2f}") #소수점 둘쨰 자리까지 포맷