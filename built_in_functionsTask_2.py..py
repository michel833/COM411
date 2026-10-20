print("Program started")
print("please enter ASCII code")
code= int(input())
if code >= 32 and code <= 126:
    print(f" the character represented by ASCII value {code} is {chr(code)}")
else:
    print("the character error")
print("program ended")