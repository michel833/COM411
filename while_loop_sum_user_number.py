print("How many numbers should i sum up?")
number_to_sum = int(input())
running_total = 0
summed = 0
while summed < number_to_sum:
  print(f"please enter number {summed} is {number_to_sum}")
  number= int(input())
  summed =summed+1
  running_total = running_total + number
print(f"the answer is {running_total}")