import random

def generate_number():
  digits = random.sample(range(1, 10), 4)
  return ''.join(map(str, digits))

def get_score(secret, guess):
  bulls = 0
  cows = 0

  for i in range(4):
    if guess[i] == secret[i]:
      bulls += 1

  for i in range(4):
    if guess[i] != secret[i] and guess[i] in secret:
      cows += 1

  return bulls, cows

def main():
  secret = generate_number()
  attempts = 0
  print("Guess the 4-digit number")

  while True:
    guess = input("\nEnter your guess: ").strip()
    attempts += 1
    if guess == secret:
      print(f"You win! The number was {secret}. Attempts: {attempts}")
      break
    
    bulls, cows = get_score(secret, guess)
    print(f"{bulls} Bulls, {cows} Cows")

if __name__ == "__main__":
  main()
