import random

guessed_words = 0  # number of guessed words
unsolved_words = 0  # number of unsolved words

while True:

	words = ["pizza", "dog", "cat", "cheese", "hotdog", "ferrari", "mercedes", "audi", "maria", "daniil", "toyota"]  # list of words

	word = random.choice(words)  # random choose the word from list
	letter = list(word)  # create a list of letters
	random.shuffle(letter)  # shuffle the list of letters
	jumbled_word = "".join(letter)  # join the list of letters to one word

	start_the_game = input("\nDo you want to start the game? (yes/no): ")  # ask the user if he wants to start the game

	if start_the_game == "yes" or start_the_game == "Yes":  # if he wants to start the game

		print("\nYou have only 3 attempts. Try to guess this word : ", jumbled_word)  # the first try is to guess the word

		amount = 0  # amount of attempts
		attempts = 2  # number of attempts



		while amount < 3:  # while the amount of attempts is less than 3 - he still to try to guess the word

			answer = input("\nYour answer is : ")  # ask the user to guess the word

			if answer.casefold() == word.casefold():  # if the answer is the word
				print("\nCongratulations! You guessed the word!")  # print the congratulations message
				guessed_words += 1  # increase the number of guessed words
				break  # break the loop
			elif attempts == 0:  # if the number of attempts is 0
				print("\nSorry, you ran out of attempts. The word was : ", word.title() )  # print the ran out message and answer
				unsolved_words += 1  # increase the number of unsolved words
				break  # break the loop
			else:  # if the answer is not the word
				print(f"\nSorry, try again! (you have {attempts} attempts)")  # print the error message

			attempts -= 1  # decrease the number of attempts
			amount += 1  # increase the amount of attempts

	elif start_the_game == "no" or start_the_game == "No":  # if he doesn't want to start the game
		break  # break the loop

total = guessed_words - unsolved_words  # total number of words guessed and unsolved
print("\nThanks for playing!", f"Your score is : {total}\n", f"\nGuessed words amount : {guessed_words}", f"\nUnsolved words amount : {unsolved_words}" )  # print the final message