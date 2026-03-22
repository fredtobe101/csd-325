#Fred Costello
#03/22/2026
#M1 Assignment 1.3
#Code Purpose: This code receives input from the user to countdown how many bottles of beer are on the wall.
#Resources used: 1 Stack Overflow "Trying to code 99 Bottles of beer on the wall"
                #2 invent with python "Exercise 23: 99 Bottles of beer on the wall"
                #3 Microsoft Copilot




def beer_countdown(bottles):
    # Count down function from the given number of bottles to 1
    for num in range(bottles, 0, -1):
        if num > 1:
            print(f"{num} bottles of beer on the wall, {num} bottles of beer! Take one down, pass it around, {num-1} bottles of beer on the wall.")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer!")
    # Function ends here and returns control to main program


def main():
    # Ask the user for the starting number of bottles on the wall
    try:
        start_num = int(input("How many bottles of beer are on the wall? "))
        beer_countdown(start_num)
        print("\nTime to buy more bottles of beer!")
    except ValueError:
        print("Please enter a valid number.")


# Run the program
main()

