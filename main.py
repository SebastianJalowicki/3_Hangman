import random
import os
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

#Test code....
# print(f'The solution word is {chosen_word}')

#Create blanks
display = []
for _ in range(word_lenght):
    display += '_'

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if guess in display:
        print(f"You've already guessed {guess}.")
    # Check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose.')

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('You win')

    print(hangman_art.stages[lives])





