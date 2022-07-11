print()
print("                              Welcome to Cows and Bulls!")
print()
print("                     Player 2 guesses player 1's three digit number.")
print()
print("A Cow is a correct number in the WRONG position and a Bull is a CORRECT number in the correct position!")
print()
secret_num1 = input("Player 1 - please enter the 1st of three digits: ")
secret_num2 = input("Player 1 - please enter the 2nd of three digits: ")
secret_num3 = input("Player 1 - please enter the 3rd of three digits: ")
print()
num1_guess = ""
num2_guess = ""
num3_guess = ""
Cows = 0
Bulls = 0
guess_count = 0
guess_limit = 10
out_of_guesses = False

while num1_guess != secret_num1 or num2_guess != secret_num2 or num3_guess != secret_num3 and not out_of_guesses:
    if guess_count < guess_limit:
        num1_guess = input("Player 2 - please enter a guess for 1st digit: ")
        num2_guess = input("Player 2 - please enter a guess for 2nd digit: ")
        num3_guess = input("Player 2 - please enter a guess for 3rd digit: ")
        if num1_guess == secret_num1:
            Bulls += 1
        elif num2_guess == secret_num1 or num3_guess == secret_num1:
            Cows += 1
        if num2_guess == secret_num2:
            Bulls += 1
        elif num1_guess == secret_num2 or num3_guess == secret_num2:
            Cows += 1
        if num3_guess == secret_num3:
            Bulls += 1
        elif num1_guess == secret_num3 or num2_guess == secret_num3:
            Cows += 1
        print()
        print(("COWS  = "),(Cows), ("(digit(s) in the WRONG position)"))
        print(("BULLS = "),(Bulls), ("(digit(s) in the CORRECT position)"))
        print()
        Cows = 0
        Bulls = 0

        guess_count += 1
        print((guess_count), ("guess(es) so far..."))
        print()
        if guess_count == guess_limit - 1:
            print("This is your last guess...")
            print()

    else:
        out_of_guesses
        print("That's 10 guesses! Sorry you LOSE!!!")
        break

else:
    Bulls == 3
    print("3 Bulls!!! YOU WIN!!!")
