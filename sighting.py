
def display_menu():
    """
    Prints the help menu.
    """
    print("Help")
    print("====")
    print("The following commands are recognized:")
    print("Display help            wildlife> help")
    print("Exit the application    wildlife> exit")

def main():
    """
    Displays the help menu and repeatedly prompts the user for a command.
    
    Commands:
    - help: Displays the help menu.
    - exit: Exits the application.
    
    Outputs an error message for unrecognized commands.
    """
    display_menu()  # Display the help menu initially
    while True:
        command = input("wildlife> ")  # Prompt the user for a command
        if command == "help":
            display_menu()  # Display the help menu if the command is 'help'
        elif command == "exit":
            print("Exiting the application.")
            break  # Exit the loop and the application if the command is 'exit'
        else:
            print("Error: Unrecognized command. Please try again.")  # Output an error message for unrecognized commands

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
