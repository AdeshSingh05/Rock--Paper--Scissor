import random 

print("You are playing a game !!")
choices= ["Rock" , "Paper" , "Scissor"]

while True:
    computer_choice = random.choice(["Rock" , "Paper" , "Scissor"])
    user_choice = input("Enter your choice: ").capitalize().strip()
    if user_choice not in choices:
      print("Invalid choice, choose stone , paper or scissor")
      continue

    print(f"Computer chose {computer_choice} , you chose {user_choice}")

    if user_choice == computer_choice:
       print("It's a tie")
    else:
       if (user_choice == "Rock" and computer_choice == "Scissor"):
        print("You won...")
       elif (user_choice == "Paper" and computer_choice == "Rock"):
        print("You won...")
       elif (user_choice == "Scissor" and computer_choice == "Paper"):
        print("You won...")
       else: 
        print("Computer won..!!")

    play_again = input("Do you want to play again (yes/no): ").lower()
    if play_again != "yes":
      print("Thank you for playing the game")
      break


