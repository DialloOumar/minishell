import sys


def main():

    while True:
        sys.stdout.write("$ ")

        commands = ["exit", "echo", "type"]
        
        # Get use input
        user_input = input()

        command = user_input.split(" ")[0]
        args = user_input.split(" ")[1]
        # Handle  the exit command
        if "exit" == command:
            return 
        if command.startswith("echo"):
            print(user_input[5:])

        elif command == "type" and args in commands:
            print(f"{args} is a shell builtin")
        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()
