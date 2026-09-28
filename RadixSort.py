import random, os, time

numbers = []
for i in range(100):
  numbers.append(random.randint(1, 999))
#print(numbers)
#The numbers can be changed

repeattime = len(numbers)

y = 0

#print(numbers[7])
#print(10**y)
#print(numbers[7]%(10**y))

#I could have just used digits.count(x-1)
while max(numbers)//(10**y) != 0:
  
  count = [0] * 10
  for x in range(repeattime):
    digitOfNum = numbers[x] // (10**y)
    digitOfNum %= 10
    count[digitOfNum] += 1

  count[0] -= 1
  for x in range(1, 10):
    #Made the range 11 to include x-2 (x-2 stopped at the 10th item)
    count[x] += count[x - 1]
  
  sortedList = numbers.copy()
  for x in range(1, len(numbers) + 1):
    num = numbers[-x]
    digitOfNum = num // (10**y)
    digitOfNum %= 10
    index = count[digitOfNum]
    sortedList[index] = num
    count[digitOfNum] -= 1
  
  y += 1
  numbers = sortedList
print(numbers)