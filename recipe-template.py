# templete
ingred = {}
choice = None 
while choice != "0": 
  print( """ Menu
        0 - Exit 
        1 - Start Recipe 
        2 - View Recipe
        """)

  choice = input("Choice: ") 
  print() 
  if choice == "0": 
    print("Good-bye.") 
  elif choice == "1": 
    name = input("Recipe Name: ")
    ptime = input("Prep Time: ")
    ttime = input("Total Time: ")
    entry = input("What is the ingredients name?: ")
    instruc = input("\nWhat are the instructions?: ")
    ingred[entry] = instruc
    print("\n", entry, "has been added.")
  elif choice == 2:
    print (name,"\n", ptime, "\n", ttime, "n\", ingred)
  else: print("Invalid choice")