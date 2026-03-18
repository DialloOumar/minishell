import sys
import os

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
                program_name = args[0]
                is_path_found = False
                for path in os.environ["PATH"].split(os.pathsep):
                    # print(path)
                    full_path = os.path.join(path, program_name)
                    # print(full_path[10:])
                    if os.path.isfile(full_path):
                        is_path_found = True
                        if os.access(full_path, os.X_OK):
                            print(f"{args[0]} is {full_path}")
                if not is_path_found:
                    print(f"{args[0]} not found")
        else:
            print(f"{command}: not found")

if __name__ == "__main__":
    main()
