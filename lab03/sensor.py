

threshold = float(input())
n = int(input())

cnt_error = 0
exceeding = 0
total_sum = 0
cnt_valid = 0
mx = -float("inf")

for i in range(n):
    indication = input()
    if indication == "error":
        cnt_error += 1
    else:
        temp = float(indication)
        cnt_valid += 1
        total_sum += temp
        
        if temp > threshold:
            exceeding += 1
        if temp > mx:
            mx = temp

avg = total_sum / cnt_valid

print(n)
print(cnt_error)
print(exceeding)
print(f"{mx:.1f}")
print(f"{avg:.1f}")
