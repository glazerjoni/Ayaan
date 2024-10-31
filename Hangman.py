import random
from HalloweenWords import words
from colorama import Fore, Back, Style

alphabetTogether = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = list(alphabetTogether)

gamePlay = 0

#colors
green = '\033[0;32m'
FG_RED = '\033[31m'
FG_GREEN = '\033[32m'
FG_WHITE = '\033[0;37m'
FG_WHITE_BOLD = '\033[1;37m'
FG_Yellow = '\033[33m'
FG_CYAN = '\033[36m'
FG_GREEN_BOLD = '\033[1;32m'
FG_RED_BOLD = '\033[1;31m'

#check whether the letter typed is in the alphabet
def check_for_alphabet(input_string):
  if input_string in alphabet_list:
    return True
  else: return False

#find all instances of the same letter in a word
def find_all_indices(string, letter):
  indices = []
  for i, char in enumerate(string):
    if char == letter:
      indices.append(i)
  return indices

#randomly choose a word
def get_valid_word(words):
  rand_word = random.choice(words)
  while '_' in rand_word or ' ' in rand_word:
    rand_word = random.choice(words)

  return rand_word

#gameplay
def game(word):
  count = 0    #this count is how much wrong tries
  candy = 0
  Guess_list = []
  split_word = list(word)
  a = set(split_word)
  size = len(split_word)
  right_list = []
  right_list=['_']*size  
  print("Guess the word", *right_list, " (", size, "letters)")
  myset = set(Guess_list)
  Guess_list = list(myset)
  Guess_list_nostyle = Guess_list

  while count < 7:
    myset = set(Guess_list)
    Guess_list = list(myset)
    print(FG_WHITE + "These are your guesses", *Guess_list, "\n")
    inputVar = input(FG_Yellow + "Please guess a letter... ")
    inputVar = inputVar.lower()
    #print(Guess_list_nostyle)

    if check_for_alphabet(inputVar):
      if inputVar not in Guess_list_nostyle:
        if inputVar in split_word:
          result = find_all_indices(split_word, inputVar)
          i = 0
          while i < len(result):
            right_list[result[i]] = inputVar
            i += 1

          Guess_list.append(Fore.GREEN + inputVar + Style.RESET_ALL)
          #Guess_list.append(inputVar)
          Guess_list_nostyle.append(inputVar)
          print (FG_GREEN + "CORRECT!")
          print(FG_WHITE + "Your word so far: ", end=" ")
          print(FG_WHITE_BOLD,  end=" ")
          print(*right_list)
          candy +=1
          print(FG_GREEN + "You have earned ", candy, "Candy!")

          b = set(right_list)
          if a == b:
            print(FG_GREEN_BOLD + "Congratulations! You have guessed the word and that is... ", word.upper())
            break

        else:
          count += 1
          Guess_list.append(Fore.RED + inputVar + Style.RESET_ALL)
          #Guess_list.append(inputVar)
          Guess_list_nostyle.append(inputVar)

          print(FG_RED + "That is INCORRECT!")
          print(FG_WHITE + "Your word so far: ", end=" ")
          print(FG_WHITE_BOLD,  end=" ")
          print(*right_list)

          if count == 7:
            print(FG_RED_BOLD + "You lose!!", "The correct word was ", FG_Yellow + word.upper())
            break
      else:
       # print (count)
        #count -= 1
        print(FG_CYAN + "\nYou've already guessed that letter\n")
    else:
      print("Please type a letter of the Alphabet")

while gamePlay>=0:
  if gamePlay >0: 
    playAgain = input (FG_WHITE_BOLD + "\nDo you want to play again? (y/n)")
    if (playAgain.lower() == "y"): 
      rand_word = get_valid_word(words)
      print ("\n")
      game(rand_word)
    else: 
      print(FG_GREEN_BOLD + "Goodbye")
      break
  else:
    gamePlay += 1
    rand_word = get_valid_word(words)
    game(rand_word)
  

