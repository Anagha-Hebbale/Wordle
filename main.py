print("Welcome to Wordle!")

secret="apple"
print("Guess the 5-Letter Word:")
guess=input()
code=[]
i=0
if guess==secret:
        print("The word is",secret,"!")

else:
    for i in range(5):
          if guess[i]==secret[i]:
                code.append("green")
          elif guess[i] in secret:
                code.append("yellow")
          else:
                code.append("grey")

print(code)           
        
    
   