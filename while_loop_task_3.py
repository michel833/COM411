print("How many bars should be charged?")
bars_to_charge=int(input())
Charged_Bars = 0
while Charged_Bars < bars_to_charge:
    print(f"Charging:{bars_to_charge* Charged_Bars} ")
    Charged_Bars = Charged_Bars + 1
print("the battery is fully charged")