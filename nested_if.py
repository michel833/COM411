print("what type of covers does the book have?")
type_of_cover = input()
print("the book has a soft cover")
if type_of_cover == "soft cover" :
     print("is the book perfect_bound")
     perfect_bound = input()
     if perfect_bound == "yes" :
      print("soft_cover, perfect_bound books are very popular")
    else :
              print("soft_cover with coils")
else:
print("books with hard covers can be more expensive!")