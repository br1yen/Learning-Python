list_animals = ["dog", "ant", "whale", "spider", "seagull", "anteater", "salamander", "lynx", "human", "clownfish"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
guess = input("I have a list of 10 animals, guess the name of one animal in my list: ")
if guess in list_animals:
    print(f"You guessed a {values[list_animals.index(guess)]} point animal")
else:
    print("You contributed a new animal! \nThe animal list is scored 1-10 from common to rare.")
    new_value = input("Give a point value (1-10) to the new animal you added to the list: ")
    list_animals.append(guess)
    values.append(int(new_value))
print(f"The list of animals was: {list_animals})")
print("Total points in list: " + str(sum(values)))
print("Goodbye, player.")

