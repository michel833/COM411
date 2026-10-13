print("where should i look?")
location = input()
if location == "in_the_bedroom":
       print("where in the bedroom should i look?")
       location_bedroom = input()
       if location_bedroom == "under_the_bed":
           print("found some shoes but no phone")
       else :
           print("found some mess but no phone.")
elif location == "bathroom":
        print("where in the bathroom should i look?")
        location_bathroom = input()
        if location_bathroom == "in_the_bathtub" :
            print("found a rubber duck but no phone")
        else :
            print("found bathroom stuff but no phone")
elif location == "living_room":
        print("where in the living room should i look?")
        location_living_room = input()
        if location_living_room == "on_the_table" :
         print("yes! I found my phone!")
     else :
         print("found some stuff but no phone")
else:
print("I do not know where that is but i will keep looking")