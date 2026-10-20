def sum_weights(character_weights, inventory_weights):
    total_weights = (character_weights + inventory_weights)
    return total_weights

def calc_avg_weights(character_weights, inventory_weights):
    avg_weights = (character_weights+inventory_weights/2)
    return avg_weights

def run():
   print("what is the weight of the character?")
   character_weights = float(input())
   print("what is the inventory weight")
   inventory_weights =float(input())
   print("what would you like to calculate")
   action= input()
   if action == "sum":
     answer= sum_weights (character_weights, inventory_weights)
     print(f"the sum of the weights is {answer: .2f}")
   elif action == "average":
    print(f"the average of the weights is {answer: 2f}")
   else:
    print("I am not sure what you would like to do")
run()
