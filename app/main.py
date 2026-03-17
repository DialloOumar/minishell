import sys


def main():

    while True:
        sys.stdout.write("$ ")
        
        # Get use input
        command = input()

        if "exit" == command:
            return 
        
        print(f"{command}: not found")


if __name__ == "__main__":
    main()
