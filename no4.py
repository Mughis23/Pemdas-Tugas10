buah1 = ["apel", "jeruk", "mangga"]
buah2 = ["apel", "anggur", "nanas"]

buah3=buah1.copy()
buah3.extend(buah2)
filter=set(buah3)
buahDewi=sorted(filter)
print("Buah yang dimiliki Dewi ", buahDewi)