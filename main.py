import random
import time
print("This is a game where I will choose a number between 1-9.")
time.sleep(1)
print("And you have to guess the number.")
time.sleep(2)
print("If you guess correctly, you will win.")
time.sleep(2)
print("Other wise you will loose")
time.sleep(2)
name = input("Oh, I almost forgot to ask your name...\nEnter your name: ")
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
time.sleep(2)
print("Alright lets step it up a bit")
time.sleep(1)
print(f"{name}, This time I am going to choose a number")
time.sleep(1)
print("Between 0-70")
time.sleep(1)
print("And same as last time you will have 3 chances")
time.sleep(1)
print("Ready?")
time.sleep(1)
print("Let's go!")
n = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,70
time.sleep(1)
print("Let's see if you can win")
z = random.choice(n)

x = 1
  while x <= 3:
    guess = int(input("Take a guess: "))
    x += 1
    if guess == z:
      print("Damn! you won!")
      break