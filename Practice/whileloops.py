num = 6
intent = "y"	
while intent == "y":
	guess = input("Guess a number 1-10: ")
	if guess == '6':
		print("You got it right!")
		break
	else:
		print("You got it wrong :(")
		intent = input("Play again? y/n")
print("Thank you for playing the game.")

num = 7
print("Heres another game.")
while True:
	guess = input("Guess a number 1-10: ")
	if guess == '7':
		print("You got it right!")
		break
	else:
		print("You got it wrong :(")
		if input("Play again? y/n") == 'n':
			break
print("Thank you for playing the game.")


	