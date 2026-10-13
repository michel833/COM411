print("what word do you see?")
hello=input()
print("\nDisplaying index position...\n")
for count in range(0,len(hello),1):
    print(f" index {count}:, {hello[count]}")
print("Done!")


