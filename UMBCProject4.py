### Setup Section ###

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")


# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in actual):

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == actual[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        
        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
        
    # ...but if the letter is not in the word at all...
    else:
      
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
      
    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

# Function to get six letter word from user
def getUserWord():

  #Set up blank input
  userWord = ""

  #while loop for user input unless equal to 6
  while(len(userWord) != 6):

    #return to message if input wrong 
    userWord = input("Enter a 6 letter word, all lower case: ")
    print()

  #return user input
  return(userWord)


### Main Program ###


#Introduction of Game 
print("WELCOME TO THE WORD GAME!")
print("===========")
print("You get six chances to enter the correct SIX LETTER WORD")
print("If the letter is in the correct place it will be marked GREEN")
print("If the letter is in the word but placed wrong, it will be YELLOW")
print("If the letter is not in the word at all it will be Red")
print()

#Set up secret word value and blank user guess value
secretWord = "steven"
userGuess = ""


#run questions 6 times 
for index in range(6):

  #set blank value for user input 
  userWord = ""

  #collect user input
  print()
  userGuess = getUserWord()
  print()

  #if guess is correct print YOU WIN 
  if(userGuess == secretWord):
    printGuessAccuracy(userGuess, secretWord)
    print()
    print("YOU WIN!")

  #Run six letter word through print accuracy function 
  else:
    printGuessAccuracy(userGuess, secretWord)
    
#Print loss statement after 6 cycles     
print()
print("YOU LOSE")





