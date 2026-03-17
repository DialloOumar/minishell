import sys


def main():

    while True:
        sys.stdout.write("$ ")
        
        # Get use input
        command = input()

        # Handle  the exit command
        if "exit" == command:
            return 
        
        if command.startswith("echo"):
            print(command[5:])
        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()
