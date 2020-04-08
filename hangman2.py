##### Every program starts with variables: 

    # the hangman word to guess
    # what the user has guessed so far
    # max # of attempts


#### Next you'll need a loop to keep asking the user for their guess

    # The game should keep running as long as there are attempts remaining
    # At each iteration of the loop, it should prompt the user to guess a letter
    # If the user guesses it right, the blanks should be replaced by what the user guessed
    # If the user guesses it wrong, it should print what the user has guessed so far along with the remaining guesses



#### Your program should end when:

    # the user has guessed all of the blanks
    # the user runs out of guesses, and it should print game over

#### What you'll need:

# 1) A string containing the original phrase

# 2) A dictionary storing the letters of the hangman phrase
    # It should have this format: position: {letter: status}
        # POSITION of the letter
        # the LETTER itself
        # STATUS of the letter: guessed/not guessed
    
    # This is what the generated dictionary looks like. Notice how it has a NESTED structure.
    # guessed_word = {
    #     0: {'H': False}, 
    #     1: {'E': False}, 
    #     2: {'L': False}, 
    #     3: {'L': False}, 
    #     4: {'O': False}, 
    # }

# 3) An integer to keep track of the remaining guesses

########### IMPORTANT: YOUR PROGRAM MUST WORK NO MATTER WHAT THE HANGMAN WORD IS ###########

#### code here ####


correct_word_phrase = "hello"
guessed_word_phrases = {}
max_attempt = 3

while attempts > 0 and guessed:
    user_guess = input("Enter a character or Guess the entire phrase")
    if (user_guess not in ):
        attempt -= 1           
    

    

    
        
    

