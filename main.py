print("Welcome to Wordle!")

import random
words = ["apple", "grape", "chair", "house", "table","water","radio","crazy","audio","ocean","fruit","truck"
         ,"plant","light","night","sound","music","dance","smile","laugh","happy","angry","sadly","quick",
         "brown","green","black","white","small","large","short","round","square","circle","heart","stars","cloud"
         ,"river","mount","beach","helix","vivid","blaze","storm","flame","frost","globe","laser","pixel","quark"]
secret = random.choice(words)

print("Guess the 5-Letter Word:")
j=0
while j<5:
    j+=1
    guess=input()
    if len(guess)!=5:
        print("Please enter a 5-letter word.")
        j-=1
        continue
    code=[]
    for i in range(5):
          if guess[i]==secret[i]:
                code.append("green")
          elif guess[i] in secret:
                code.append("yellow")
          else:
                code.append("grey")
    print(code)  
    if guess==secret:
        print("The word is",secret,"!")
        break
if j==5:
     print("You have used all your guesses. The word was: ", secret)

        
        
    
   