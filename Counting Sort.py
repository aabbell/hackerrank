arr = [3,4,9,5,3,4,9,5,7,1]

largest = max(arr)

print(largest)

countarr = [0] * (largest + 1)

for i in arr:
    countarr[i]+=1





print(countarr)
