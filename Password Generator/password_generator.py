import secrets
import string
import os


def generate_password(desired_length, upperC, lowerC, numbs, symbs):
    password = ""

    characters = ""

    if upperC == "y":
        characters += string.ascii_uppercase

    if lowerC == "y":
        characters += string.ascii_lowercase

    if numbs == "y":
        characters += string.digits

    if symbs == "y":
        characters += string.punctuation

    while len(password) < desired_length:
        password += secrets.choice(characters)

    return password


def yes_no_valid(prompt):
    while True:
        ans = input(prompt).lower()

        if ans in ("y", "n"):
            return ans

        print("Please Enter only Y or N.")


def get_length():
    while True:
        try:
            desired_length = int(input("Length of Password: "))

            if desired_length < 1:
                print("Enter a Positive Number.")
                continue

            return desired_length

        except ValueError:
            print("Enter a Valid Number.")

def line():
    print("----------------------------")

def main():
    while True:
        os.system("clear")
        line()
        print("---- Password Generator ----")
        line()

        desired_length = get_length()
        upperC = yes_no_valid("Include Uppercases? y/n : ")
        lowerC = yes_no_valid("Include Lowercases? y/n : ")
        numbs = yes_no_valid("Include Numbers? y/n : ")
        symbs = yes_no_valid("Include Symbols? y/n : ")
    
        if upperC == "n" and lowerC == "n" and numbs == "n" and symbs == "n":
            print("Choose at least one option.")
            input("Please Enter to Try Again...")
            continue

        password = generate_password(
           desired_length,
           upperC,
           lowerC,
           numbs,
           symbs,
           )

        print(f"Password = {password}")
        break


if __name__ == "__main__":
    main()
