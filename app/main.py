import sys


def main():
    sys.stdout.write("$ ")
    
    # Get use input
    command = input()
    print(f"{command}: not found")


if __name__ == "__main__":
    main()
