from random import choice, randint

def separator():
  print('\n' + 20 * "=" + '\n')


coin = ["Heads", "Tails"]
count = int(input("How many times to flip the coin? "))
while count > 0:
  flip = choice(coin)
  print(flip)
  count -= 1

bonuses = [100, 200, 300, 400, 500]
bonus = choice(bonuses)

separator()

# let user define finish line 
finish = int(input("\nHow many steps to the finish line? "))
# start runners at start line 
runner1 = 0
runner2 = 0
while runner1 < finish and runner2 < finish:
  # move runners forward random number of steps
  runner1 += randint(1,5)
  runner2 += randint(1,5)
  print("\nRunner 1 is now at", runner1)
  print("Runner 2 is now at", runner2)

if runner1 == runner2:
  print("It's a tie")
elif runner1 > runner2:
  print("Runner 1 wins")
else:
  print("Runner 2 wins")


separator()

while True:
  high = input("Highest number for guess? ")
  computer = randint(1,int(high)) # random int between 1 and 100
  #print(computer)
  tries = 1
  guess = int(input("Guess a number between 1 and " + high + ": "))
  while guess != computer:
    if guess > computer:
      print("Sorry, your guess is too high, try again")
    else:
      print("Sorry, your guess is too low, try again")
    tries += 1
    guess = int(input("Guess a number between 1 and " + high + ": "))
    
  print("Congratulations, you guessed it in", tries, "tries")



