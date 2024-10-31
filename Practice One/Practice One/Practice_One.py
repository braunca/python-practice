


#initialize the variables
knightdescription = " " 
boydescription = " " 
walkdescription = " " 
knightname = " "
boyname = " "
animal = " "
gift = " " 
answer = " "

#Ask the user to specify values for the variables
knightname = input("Enter a knights's name: ")
boyname = input("Enter a boy's name: " )
animal = input("Name a type of animal: " )
gift = input("Name something you find in the bathroom: ")
knightdescription = input("Enter a description of a knight: ")
boydescription = input("Enter a description of a car: ")
walkdescription = input("Enter a description of how you might walk: " )
answer = input("What would you say to someone who gave you a cow: ")

#Display the story
print ("Once upon a time,")
print("there was a knight named " + knightname.capitalize() + ".")
print("One day, " + knightname.capitalize() + " was walking " + walkdescription.lower() + " down the street.")
print("Then the knight met a " + boydescription.lower() + " boy named " + boyname.capitalize() + ".")
print("He said, 'You are really " + knightdescription.lower() + "!'")
print("They said '" + answer.capitalize() + ", " + boyname.capitalize() + ".'")
print("Then they both rode away on a " + animal.lower() + " and became knight and squire.")
