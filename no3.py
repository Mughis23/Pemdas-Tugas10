buah = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
result = []

for x in buah:
    if len(buah) >=5:
        result.append(buah)
result.sort()
print("Output : ", result)