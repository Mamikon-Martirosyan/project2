import random


def get_random_word(wordlist):
  """Generates a random word from a wordlist.

  Args:
    wordlist: A list of words.

  Returns:
    A random word from the wordlist.
  """

  return random.choice(wordlist)

def draw_hangman(chances):
    if chances == 6:
        print("________ ")
        print("|  | ")
        print("| ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 5:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 4:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| / ")
        print("| ")
        print("| ")
    elif chances == 3:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /| ")
        print("| ")
        print("| ")
    elif chances == 2:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| ")
        print("| ")
    elif chances == 1:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| / ")
        print("| ")
    elif chances == 0:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| / \ ")
        print("| ")
# def draw_hangman(chances):
#   """Draws the hangman figure based on the number of chances remaining.

#   Args:
#     chances: The number of chances remaining.
#   """

#   if chances == 6:
#     print('________')
#     print('| |')
#     print('O ')
#     print('| ')
#     print('| ')
#     print('| ')
#   elif chances == 5:
#     print('________')
#     print('| |')
#     print('O ')
#     print('|/')
#     print('| ')
#     print('| ')
#   elif chances == 4:
#     print('________')
#     print('| |')
#     print('O ')
#     print('|/')
#     print('\| ')
#     print('| ')
#   elif chances == 3:
#     print('________')
#     print('| |')
#     print('O ')
#     print('|/')
#     print('\|/')
#     print('| ')
#   elif chances == 2:
#     print('________')
#     print('| |')
#     print('O ')
#     print('|/')
#     print('\|/')
#     print('|')
#   elif chances == 1:
#     print('________')
#     print('| |')
#     print('O ')
#     print('|/')
#     print('\|/')
#     print('|')
#   elif chances == 0:
#     print('________')
#     print('| |')
#     print('O ')
#     print('|/')
#     print('\|/')
#     print('|')
#     print('Game over!')


def play_game(word):
  """Plays the Hangman game.

  Args:
    word: The word to be guessed.
  """

  chances = 6
  guessed_letters = []

  while chances > 0:
    # Display the current word and the number of chances remaining.
    print('Current word:', guessed_letters)
    print('Chances remaining:', chances)

    # Get the player's guess.
    letter = input('Guess a letter: ')

    # Check if the letter is in the word.
    if letter in word:
      # Add the letter to the guessed letters list.
      guessed_letters.append(letter)

      # Check if the player has guessed the entire word.
      if all(letter in guessed_letters for letter in word):
        print('You win!')
        break
    else:
      # Subtract a life from the player.
      chances -= 1

    # Draw the hangman figure.
    draw_hangman(chances)

    # If the player has run out of chances, the game is over.
    if chances == 0:
      print('Game over!')


if __name__ == '__main__':
    # Generate a random word from the wordlist.
    word = get_random_word(['apple', 'banana', 'cat'])

  # Play the game.
    play_game(word)




