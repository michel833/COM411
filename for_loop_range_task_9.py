print("what level of brightness is required?")
level_of_brightness = int(input() )
print("\n Adjusting brightness level...\n")
for level_of_brightness in range(2, level_of_brightness+1, 2):
    print (f"level of brightness : {'*'*level_of_brightness}")
print("complete!")
