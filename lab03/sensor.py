threshold = int(input())
n = int(input())
cnt_error = 0
exceeding = 0
avg = 0
cnt = 0
mx = 0
for i in range(n):
    indication = input()
    if indication == 'error':
        cnt_error += 1
    else:
        indication = float(indication)
        cnt += 1
        avg += indication
        if indication > threshold:
            exceeding += 1
        if indication > mx:
            mx = indication
h = avg/cnt
print(n)
print(cnt_error)
print(exceeding )
print(f"{mx:.1f}")
print(f"{h:.1f}")

        

        
