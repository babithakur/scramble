import random
words = ["python", "java", "ruby", "perl", "roshan", "saru", "cyper",
             "hacker", "anonymous", "metasploit", "malang", "goat", "love",
             "omega", "programming", "coding", "music", "website", "javascript",
             "laptop", "wireshark"]
#shuffled = ''.join(random.sample(word, len(word)))
print("GUESS THE WORD :)\n")
def game():
    shuffled = []
    for i in words:
        shuffled.append(''.join(random.sample(i, len(i))))
    a = random.randint(0, len(shuffled) - 1)
    guess = input(f"Guess the word {shuffled[a]}: ")
    if guess == words[a]:
       print("Congrats! You got it :)\n")
       again = input("Do you wanna play again? (Y or N): ")
       if again == "Y" or again == "y":
           game()
       else:
           print("See you again!")
    else:
       while guess != words[a]:
           print("It's incorrect!\n")
           guess = input(f"Please guess the word {shuffled[a]} again: ")
           if guess == words[a]:
               print("Congrats! You got it :)\n")
               again = input("Do you wanna play again? (Y or N): ")
               if again == "Y" or again == "y":
                   game()
               else:
                   print("See you again :)")

if __name__=='__main__':
    game()