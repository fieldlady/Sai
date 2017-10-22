"""This is Sai's first real project - to write a Mad Libs story! I will build a program that does the following: 
1.Prompt the user for input.
2.Print the entire Mad Libs story with the user's input in the right places."""

print "Hey Guys! Mad Lib is starting now!"
Main_Character = raw_input("Please enter a name for the main character: ")
Adjective_1 = raw_input("Please enter your 1st adjective: ")
Adjective_2 = raw_input("Please enter your 2nd adjective: ")
Adjective_3 = raw_input("Please enter your 3rd adjective: ")
Verb_1 = raw_input("Please enter your 1st Verb: ")
Verb_2 = raw_input("Please enter your 2nd Verb: ")
Verb_3 = raw_input("Please enter your 3rd Verb: ")
Noun_1 = raw_input("Please enter your 1st Noun: ")
Noun_2 = raw_input("Please enter your 2nd Noun: ")
Noun_3 = raw_input("Please enter your 3rd Noun: ")
Noun_4 = raw_input("Please enter your 4th Noun: ")
Animal = raw_input("Please enter an animal: ")
Food = raw_input("Please enter a food: ")
Fruit = raw_input("Please enter a fruit: ")
Number = raw_input("Please enter a number: ")
Superhero = raw_input("Please enter a superhero name: ")
Country = raw_input("Please enter a country: ")
Dessert = raw_input("Please enter a dessert: ")
Year = raw_input("Please enter a year: ")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY %(Adjective_1,Main_Character,Verb_1,Adjective_2,Noun_1,Noun_2,Animal,Food, Verb_2, Noun_3, Fruit, Adjective_3,Main_Character, Verb_3,Number, Main_Character,Superhero,Superhero,Main_Character,Country, Main_Character, Dessert,Main_Character,Year,Noun_4)