# Advent Of Code 2020 Day 1
arr = []
with open('input.txt', encoding='utf8') as f:
    for line in f:
        arr.append(line.strip())
j = 1
result_arr = []

for i in range(0,len(arr)):
    for j in range(1,len(arr)):
        result = int(arr[i]) + int(arr[j])
        if result == 2020:
            result_arr.append(int(arr[i])*int(arr[j]))
    else:
        pass
print(result_arr)
