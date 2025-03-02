import sys
import time
import random

def type_like_typing(text):
    """Simulates typing effect under TMTC: header"""
     # Static "TMTC: " header (NOT animated)
    sys.stdout.write("TMTC: ")
    sys.stdout.flush()
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.05))

logo = """
████████╗██████╗  █████╗ ██╗███╗   ██╗███╗   ███╗███████╗████████╗ ██████╗  ██████╗ ██████╗ ██████╗ ███████╗
╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║████╗ ████║██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝
   ██║   ██████╔╝███████║██║██╔██╗ ██║██╔████╔██║█████╗     ██║   ██║   ██║██║     ██║   ██║██║  ██║█████╗  
   ██║   ██╔══██╗██╔══██║██║██║╚██╗██║██║╚██╔╝██║██╔══╝     ██║   ██║   ██║██║     ██║   ██║██║  ██║██╔══╝  
   ██║   ██║  ██║██║  ██║██║██║ ╚████║██║ ╚═╝ ██║███████╗   ██║   ╚██████╔╝╚██████╗╚██████╔╝██████╔╝███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
------------------------------------------------------------------------------------------------------------
Version: 1.0.0
Author:  @rahfianugerah

Description:
This is a smart and interactive chatbot designed to help you 
learn coding and programming in a fun, engaging, and effective way. 

Press 'Q' or type 'exit'/'quit' for exiting the program.
------------------------------------------------------------------------------------------------------------
"""

def main():
    print(logo)
    while True:
        user_input = input("\nYou: ")
        quit_prompt = ["q", "quit", "exit"]
        if user_input.lower() in quit_prompt:
            type_like_typing("Goodbye, Have a nice day!")
            break
        else:
            type_like_typing("I don't understand what you are saying.")

if __name__ == "__main__":
    main()
