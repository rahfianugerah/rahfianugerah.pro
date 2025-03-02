# Import the required libraries
import os
import sys
import time
import random

def type_like_typing(text, max_length=102):
    """Simulates typing effect under TMTC: header with a max character limit per line"""
    sys.stdout.write("TMTC: ")  # Static header (NOT animated)
    sys.stdout.flush()
    
    char_count = 0  # Counter for characters in the current line
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.04))  # Typing effect delay

        char_count += 1  # Increment character count
    
        # Insert a new line if max_length is reached
        if char_count >= max_length and char == " ":
            sys.stdout.write("\n      ")  # Indent new line under "TMTC: "
            sys.stdout.flush()
            char_count = 0  # Reset character count for new line

logo = """
████████╗██████╗  █████╗ ██╗███╗   ██╗███╗   ███╗███████╗████████╗ ██████╗  ██████╗ ██████╗ ██████╗ ███████╗
╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║████╗ ████║██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝
   ██║   ██████╔╝███████║██║██╔██╗ ██║██╔████╔██║█████╗     ██║   ██║   ██║██║     ██║   ██║██║  ██║█████╗  
   ██║   ██╔══██╗██╔══██║██║██║╚██╗██║██║╚██╔╝██║██╔══╝     ██║   ██║   ██║██║     ██║   ██║██║  ██║██╔══╝  
   ██║   ██║  ██║██║  ██║██║██║ ╚████║██║ ╚═╝ ██║███████╗   ██║   ╚██████╔╝╚██████╗╚██████╔╝██████╔╝███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
+-----------------------------------------------------------------------------------------------------------+
 Version: 1.0.0
 Author:  @rahfianugerah
                              
 Description:
 This is a smart and interactive chatbot designed to help you
 coding and programming in a fun, engaging, and effective way.

 Press 'Q' or type 'exit'/'quit' for exiting the program.
 Press 'M' or type 'menu' for showing the main menu.
+-----------------------------------------------------------------------------------------------------------+
"""

def main():
    print(logo)
    type_like_typing("Hello! I'm TMTC, your personal chatbot that will help you learn how to code. How can I help you today? and how can i assist you?")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["q", "quit", "exit"]:
            type_like_typing("Goodbye, Have a nice day!")
            break
        elif user_input.lower() in ["m", "menu"]:
            with open("utils/menu.txt", "r") as f:
                menu = f.read()
            print(f"TMTC: {menu}")
        elif user_input.lower() in ["clear", "cls"]:
            os.system("cls" if os.name == "nt" else "clear")  # Clears console
            print(logo)
        else:
            type_like_typing("I don't understand what you are saying.")

if __name__ == "__main__":
    main()
