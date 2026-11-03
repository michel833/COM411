import csv


def export (exported_items, num_items) :
    print ("exporting...")
    with open (exported_items, "a") as file :
        for count in range(num_items) :
            print ("please enter the item id")
            item_id = int(input())
            print("please enter the item name")
            item_name = input()
            print("please enter the item color")
            item_color = input()
            data = f"{item_id} ,{item_name},  {item_color}\n"
            file.write(data) # Write the values of the variables to the CSV file i
        print ("Done!")
def run_task3 () :
    export ("exported_items.csv", 2)
if __name__ == "__main__":
        run_task3()

