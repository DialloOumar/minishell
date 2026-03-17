import sys


# supported commands
COMMANDS = ["exit", "echo", "type"]

def main():

    while True:
        sys.stdout.write("$ ")
        
        line = input()
        # Get use input
        command, *args = line.split(" ")

        # Handle  the exit command
        if "exit" == command:
            return 
        if command == "echo":
            print(line[5:])
        elif command == "type":
            if args[0] in COMMANDS:
                print(f"{args[0]} is a shell builtin")
            else:
                print(f"{args[0]} not found")
        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()
