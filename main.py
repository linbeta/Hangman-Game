import ascii_art
import word_bank_band_name
import random

answer = random.choice(word_bank_band_name.band_name_list)
digits = len(answer)
display = []
guessed_list = []
for n in range(digits):
  display += "_"

# Creating the answer_list to check if the guesses are complete because there are spaces in the answer. 
answer_list = []
for n in answer:
  if n == " ":
    n = "_"
  answer_list += n

# Game welcome interface & shows Word bank version
print(ascii_art.logo + "Band name version!\n\n")
print("Welcome to Beta's hangman game-band name version!")

# Game stages and end game condition setting:
stages = 6
end_of_game = False


# Main game structure
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  from replit import clear
  clear()
  
  if len(guess) == 1:
    # Let user know of the letter had been guessed. There is another way to do this: create a new list to store all the letters user guessed.
    if guess in guessed_list:
      print(f"Letters guessed: {guessed}")
      print(f"You've already guessed {guess}, try other letters.")
    else:
      guessed_list += guess
      guessed = ', '.join(guessed_list)
      print(f"Letters guessed: {guessed}")
    
    for position in range(digits):
      letter = answer.lower()[position]
      if letter == guess:
        display[position] = answer[position]
    print(' '.join(display))

    if display == answer_list:
      end_of_game = True
      print(f"You win!\nThe answer is {answer}")

    if guess not in answer.lower():
      print(f"There's no {guess} in this band.")
      stages -= 1
    if stages == 0:
      end_of_game = True
      print(f"You Lose...\nThe answer is {answer}")
  
  else:  
    print("Please enter a single letter. :)")
    print(' '.join(display))
  
  print(ascii_art.stages[stages])

# There's a bug: if guess = " "