
# Weight Force on the hook
hook = [0.490,0.980,1.47,1.96,2.45,3.43]

#Weight Force of the Cart
cart = [8.822,8.3922,7.9022,6.4322,6.9222,5.9422]

#Acceleration Values
a = [0.75570,1.5516,2.1623,2.7880,4.1304,5.0615]

y2 = 1
y1 = 0
finalA = 0
listA = []
for i in range(5):
    finalA += a[y2] - a[y1]
    listA.append(a[y2] - a[y1])
    y2+=1
    y1+=1


y2 = 1
y1 = 0
finalH = 0
listH = []
for i in range(5):
    finalH += hook[y2] - hook[y1]
    listH.append(hook[y2] - hook[y1])
    y2+=1
    y1+=1


y2 = 1
y1 = 0
finalC = 0
listC = []
for i in range(5):
    finalC += cart[y2] - cart[y1]
    listC.append(cart[y2] - cart[y1])
    y2+=1
    y1+=1


print(finalH/finalA)
print(finalC/finalA)