import random

comp=random.randint(1,100)
attempts=1
user=1
while(comp!=user):
    user=int(input("Guess the number:"))
    if (comp<user):
         print("Smaller number please")
         attempts+=1
    elif(comp>user):
        print("Bigger number please")
        attempts+=1
print(f"You guessed it right in {attempts} attempts " ,end="")
input("Game over!")


             
