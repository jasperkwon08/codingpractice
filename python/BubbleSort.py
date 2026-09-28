import random, os, time

numbers = []
for x in range(100):
    numbers.append(random.randint(1,999))

repeat = len(numbers)
def compare(inta, intb):
  if numbers[inta] < numbers[intb]:
    return True
  else:
    return False

for i in range(repeat):
  for j in range(repeat - i - 1):
    if(compare(j,j+1)):
      numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

numbers.reverse
print(numbers)