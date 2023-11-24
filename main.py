import random
import time
print("This is a game where I will choose a number between 1-9.")
time.sleep(2)
print("And you have to guess the number.")
time.sleep(2)
print("If you guess correctly, you will win.")
time.sleep(2)
print("Other wise you will loose")
time.sleep(2)
name = input("Oh, and I almost forgot to ask your name...\nEnter your name: ")
time.sleep(1)
print(f"Nice to meet you {name}")
time.sleep(2)
print("You will get a total of 3 chances.")
time.sleep(2)
print("Some say it is very difficult to win against me")
time.sleep(2)
print("Do you think you can win?")
time.sleep(2)
print("Let's find out!")
number = 1,2,3,4,5,6,7,8,9
c = random.choice(number)
guess_count = 1
while guess_count <= 3:
  guess = int(input("Take a guess: "))
  guess_count += 1
  if guess == c:
      print("Damn! you won!")
      break
else:
   print("Oh no... you have lost like others!")
   time.sleep(1)
   print(f"I choosed {c}")
   time.sleep(1)
   print("Better lucknext time")
  
##Medium mode
##This part has been under work
