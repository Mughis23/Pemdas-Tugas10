nomer = [7,4,9,2,5,1]
filter = []

for x in nomer:
    if x % 2 == 0:
        filter.append(x)
filter.sort()
print("Input : ", nomer)
print("Output :", filter)