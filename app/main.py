import sys


def main():

    while True:
        sys.stdout.write("$ ")

        # supported commands
        commands = ["exit", "echo", "type"]
        
        # Get use input
        user_input = input()

        command = user_input.split(" ")[0]
        # Handle  the exit command
        if "exit" == command:
            return 
        if command.startswith("echo"):
            print(user_input[5:])
        elif command == "type":
            command_arg = user_input.split(" ")
            print(f"{command_arg[1]} is a shell builtin")
        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()
