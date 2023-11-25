import random
import time
p = "Nice Job!","WOW!","You're amazing!","You're awesome!","You're smart!","Damn!"
n = "Oh no,","You are not smart,","You are not awesome,","You are not amazing,","That's sad"

print("Welcome to the quiz game!")
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
c = random.randint(0,9)
positive = random.choice(p)
negative = random.choice(n)
guess_count = 1
while guess_count <= 3:
  guess = int(input("Take a guess: "))
  guess_count += 1
  if guess == c:
      print(f"{positive} you won!")
      break
else:
   print(f"{negative}you have lost like others!")
   time.sleep(1)
   print(f"I choosed {c}")
   time.sleep(1)
   print("Better luck next time")
  

##Medium mode
##This part has been under work

print(f"{name}, Lets step it up a bit")
time.sleep(2)
print("I am going to choose a number between 0-100")
time.sleep(2)
print("And you have to take a guess\nSame rule like last time you get to guess 3 times.")
time.sleep(2)
print("Ready?")
time.sleep(1)
print("Let's go!")
number = random.randint(0, 100)
guess_count = 0
while guess_count < 3:
    guess = int(input("Take a guess: "))
    guess_count += 1
    if guess == number:
        print(f"{positive}, you won!")
        break
else:
   print(f"{negative}you have lost like others!")
   time.sleep(1)
   print(f"I choosed {c}")
   time.sleep(1)
   print("Better luck next time")

##Medium mode
##could be devloped

print(f"{name}, Lets step it up a bit")
time.sleep(2)
print("I am going to choose a number between 0-100")
time.sleep(2)
print("And you have to take a guess\nSame rule like last time you get to guess 3 times.")
time.sleep(2)
print("Ready?")
time.sleep(1)
print("Let's go!")
number = random.randint(0, 100)
guess_count = 0
while guess_count < 3:
    guess = int(input("Take a guess: "))
    guess_count += 1
    if guess == number:
        print(f"{positive}, you won!")
        break
else:
  print(f"{negative} you have lost!")
  time.sleep(1)
  print(f"I choosed {number}")
  
##Hardest difficulty level
print(f"{name},this is the hardest difficulty level")
