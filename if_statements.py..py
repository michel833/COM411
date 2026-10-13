print("what type of book of book is this?")
type_book= input()
if type_book == "adventure" :
    print("i like adventure books!")
    print("finished reading book!")

print("please enter the activity to be performed.")
activity = input()
if activity == "calculate" :
    print("performing calculations!")
else:
    print("performing activity...")
    print("Activity completed!")

print("toward which direction should i go (up, down, left, right)")
direction = input()
if direction == "up" :
    print("i will go upward")
elif direction == "down" :
    print("i will go downward")
elif direction == "left" :
    print("i will go leftward")
else :
    print("i will go rightward")

