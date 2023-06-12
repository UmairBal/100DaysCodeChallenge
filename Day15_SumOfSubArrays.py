num = [1, 2, 0, 7, 2]

for i in range((len(num))):
    result = 0
    for j in range(i, (len(num))):
        result += num[j]
        print(result)
