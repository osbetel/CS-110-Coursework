# TEST FILE



uncertaintyTimes = [0.72555,0.71831,0.68342,0.70528,0.73122,0.74642,0.69386]
uncertaintyTimes.sort()
print(uncertaintyTimes)


total = 0
num = 0


for int in uncertaintyTimes:
    total += int
    num += 1

# print(total)
# print(num)
avg = total/num
# print(avg - uncertaintyTimes[0])
print(uncertaintyTimes[6] - avg)    # Time uncertainty
print()

distance = .405 # Meters
time50 = [1.01689,1.01082,1.08266]
time100 = [0.72138,0.71469,0.73176]
time150 = [0.61324,0.62412,0.59952]
time200 = [0.50576,0.57857,0.54000]
time250 = [0.44337,0.43117,0.45492]
time350 = [0.40505,0.38453,0.41210]


temp = 0
for i in time50:
    print((2*distance)/i**2)
    temp += ((2*distance)/i**2)
print("Avg = ", temp/3)
temp = 0

print()
for i in time100:
    print((2*distance)/i**2)
    temp += ((2*distance)/i**2)
print("Avg = ", temp/3)
temp = 0

print()
for i in time150:
    print((2*distance)/i**2)
    temp += ((2*distance)/i**2)
print("Avg = ", temp/3)
temp = 0

print()
for i in time200:
    print((2*distance)/i**2)
    temp += ((2*distance)/i**2)
print("Avg = ", temp/3)
temp = 0

print()
for i in time250:
    print((2*distance)/i**2)
    temp += ((2*distance)/i**2)
print("Avg = ", temp/3)
temp = 0

print()
for i in time350:
    print((2*distance)/i**2)
    temp += ((2*distance)/i**2)
print("Avg = ", temp/3)
temp = 0