
import random
from words import word_list
from art import logo, stages


placeholder = ""
lives = 6

print(logo)


chosen_word = random.choice(word_list)
print(chosen_word)

for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_Over = False
correct_letters = []

while not game_Over:
    print(f"*******************************{lives}/6 LIVES LEFT **********************************")
    guess = input("Guess a letter : ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    
    display=""
    
    
    for letter in chosen_word:
       if letter==guess:
        display += letter
        correct_letters.append(guess)
       elif letter in correct_letters:
           display += letter
       else:
           display += "_"
           
       
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, it is not in the word")
        
        
        if lives == 0:
            game_Over = True
            
            
            print(f"*************************IT WAS {chosen_word} ! YOU LOOSE*****************************")
            
            

    if "_" not in display:
        game_Over = True
        print("You win")

print(stages[lives])
   
    
    