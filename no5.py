nomer=[105, 20, 8, 150, 30, 5, 200]
result=[]
for n in nomer:
    if 10 <= n <= 100:
       result.append(n)
result.sort()      
print("Output :",result)