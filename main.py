print("Welcome to Wordle!")

secret="apple"
print("Guess the 5-Letter Word:")
j=0
while j<5:
    j+=1
    guess=input()
    code=[]
    i=0
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

        
        
    
   