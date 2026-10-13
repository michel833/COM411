print("please enter the first whole number")
number_1 = int(input( ))
print("please enter the second whole number")
number_2 = int(input( ))
print("please enter the third number")
number_3 = int(input( ))
counter_even = 0
counter_odd = 0
if number_1 % 2 == 0 :
   counter_even = counter_even + 1
else :
    counter_odd = counter_odd +1
if number_2 % 2 == 0 :
    counter_even = counter_even + 1
else :
    counter_odd = counter_odd +1
if number_3 % 2 == 0 :
    counter_even = counter_even + 1
else :
    counter_odd = counter_odd +1
    print("there were counter error")