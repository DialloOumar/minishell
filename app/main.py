import sys
import os
import subprocess

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
        
        execute_command(command,args)


def execute_command(command, args):

    full_path = is_external_command(command)

    if command == "echo":
        result = " ".join(args)
        print(result)
    elif command == "type":
        program_name = args[0]
        full_path = is_external_command(program_name)
        if is_internal_command(program_name):
             print(f"{program_name} is a shell builtin")
        elif full_path != "":
            print(f"{args[0]} is {full_path}")
        else:
            print(f"{args[0]} not found")
    elif full_path != "":
        # Execute as an external command
        subprocess.run([command]+args)
    else:
        print(f"{command} not found")
          

def is_external_command(command_name):
    for path in os.environ["PATH"].split(os.pathsep):
        full_path = os.path.join(path, command_name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return ""

def is_internal_command(command):
    return command in COMMANDS

if __name__ == "__main__":
    main()
