
#PYTHON LOGICAL & CONCEPTUAL

data = [12, 7, 12, 5, 7, 9, 5, 12, 9, 7, 15]

count = {}

for x in data:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

print("Duplicate Values:")

for x in data:
    if count[x] > 1:
        if x in data[:data.index(x)]:
            continue
        print(x, "->", count[x],"times")
        

#Q2. Missing Number Logic

ids = [1, 2, 3, 4, 5, 7, 8, 9, 10]

for i in range(1, 11):
    if i not in ids:
        print("Missing ID:", i)
