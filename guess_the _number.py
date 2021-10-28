from random import seed
from random import randint

print("Welcome to the Guessing game!!")
print("The computer will be generating a random integer in the range 1 to 10. Your task is to generate the number correctly.")
print("You will get 5 chances.")
value = randint(1, 10)


i = 0
while(i<5):
  a = input("Enter a number from 1-10: ")
  if(a.isnumeric()):
    a = int(a)
    if a == value:
        print("You got it right!! Congratulations")
        break
        
    elif a > value:
        print("Your number is a bit high! Try Again")
        
    else:
        print("Your number is a bit low!Try Again")
        
  else:
    print("Invalid Input")
    
  i+=1
print("The number guessed by the computer is " + str(value))
