def Number_Game():
    # Number guessing game
    import random
    from termcolor import colored

    print("\n" * 2)
    while(True):
        Response = ""
        while Response.lower() != "yes":
            print()
            print(colored("Do you want to play a game?" ,"yellow"))
            Response = input("Enter Yes or No: ")
            if Response.lower() == "no":
                print("\n" * 2)
                print(colored("Oh.......well you should like really reconsider plz", "yellow"))
            elif Response.lower() == "yes":
                print()
                print(colored("Atta boy!", "yellow"))
            else:
                print()
                print(colored("Invalid response. Please enter Yes or No.", "yellow"))

        # Randomly get secret number between 1 and 20 
        Secret_Number = random.randint(1,20)
        print()
        print(colored("Okay bro, I'm thinking of a number between 1 and 20 !!", "yellow"))
        print(colored("You have 5 tries to guess what it is or else...", "yellow"))
        print()       

        # Track and validate attempts
        Attempts = 0
        while Attempts < 5:
            Guess = input(f"Attempt({Attempts + 1}): What's Your Guess? ")

            try:
                Guess = int(Guess)  

                # Check if guess if out of bounds
                if Guess < 1 or Guess > 20:
                    print()
                    print(colored("That's out of bounds, bro. Please enter a number in range.", "yellow"))
                    print()
                    continue

                # Check if guess is correct
                if Guess == Secret_Number:
                    print()
                    print(colored(f"You nailed it!! The correct number was {Secret_Number}! Dang, good looking and smart aren't ya??", "green"))
                    print()
                    break

                elif Guess < Secret_Number:
                    print()
                    print(colored("Nah bro, too low. Try again.", "yellow"))
                    print()
                elif Guess > Secret_Number:
                    print()
                    print(colored("Woah bro that's too high. It's okay though, don't give up.", "yellow"))
                    print()
                Attempts += 1

            except ValueError:
                print()
                print(colored("Invalid input. Please enter a number.", "yellow"))
                print()
                continue 

            # Out of attempts
            if Attempts == 5 and Guess != Secret_Number:
                print()
                print(colored(f"*Crying* Sorry bro, you're out of tries. The secret number was {Secret_Number}. Better luck next time!", "red"))
                print()
                break
        # Ask if user wants to play again
        print(colored("Would you like to play again?" ,"yellow"))
        Play_Again = input("Enter Yes or No: ")
        if Play_Again.lower() == "yes":
            print()
            print(colored("Restarting...", "blue"))
            print("\n" * 3)
                  
        if Play_Again.lower() != "yes":
            print("\n" * 2)
            print(colored("Alright, catch you later!", "blue")) 
            print("\n" * 2)  
            break

Number_Game()