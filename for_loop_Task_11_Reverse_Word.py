print("what phrase do you want to see in reverse?")
phrase=input()
print("\nreversing...")
print("phrase is: ")
for position in range(len(phrase)-1,-1):
    print("phrase[position], end"" ")
