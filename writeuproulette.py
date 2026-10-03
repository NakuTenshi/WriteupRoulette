#!/bin/python3

import os 
import random
from datetime import datetime

def main():
    if __file__.endswith(".py"):
        writeup_directory = "./writeups"
    else:
        writeup_directory = os.path.expanduser("~/.local/share/writeups")

    not_readed_file = os.path.join(writeup_directory , "not_readed_writeups.txt")
    readed_file = os.path.join(writeup_directory , "readed_writeups.txt")


    with open(not_readed_file, "r") as f:
        not_readed_list = [l.strip() for l in f.readlines()]
        not_readed_list_count = len(not_readed_list)

    if not os.path.exists(readed_file):
        readed_file_count = 0
    else:
        with open(readed_file, "r") as f:
            readed_file_list = [l.strip() for l in f.readlines()]
            readed_file_count = len(readed_file_list)

    date = datetime.now().date()
    todays_writeup = random.choice(not_readed_list)

    while True:
        os.system("clear")
        print(f"<<============================({date})============================>>")
        print(f"   !Readed WriteUps Count: {not_readed_list_count}")
        print(f"    Readed WriteUps Count: {readed_file_count}")

        if readed_file_count:
            print(f"    Last Readed WriteUp: {readed_file_list[-1]}")

        print(f"\nToday's WriteUp:")
        print(f"        {todays_writeup}")

        print("")
        print("['1' => Mark As Readed]\n['2' => Choice Another One]\n['3' => Remove It from List]\n['exit' OR 'quit' => Closing]")
        user_input = input("$ ")


        if user_input == "1":
            with open(readed_file , "a") as f:
                if todays_writeup in not_readed_list:
                    not_readed_list.remove(todays_writeup)
                    with open (not_readed_file , "w") as g:
                        g.write("\n".join(not_readed_list))
                        f.write(f"{todays_writeup}\n")
            break

        elif user_input == "2":
            todays_writeup = random.choice(not_readed_list)

        elif user_input == "3":
            if todays_writeup in not_readed_list:
                not_readed_list.remove(todays_writeup)
                with open (not_readed_file , "w") as g:
                    g.write("\n".join(not_readed_list))

                    not_readed_list_count = len(not_readed_list)
                    todays_writeup = random.choice(not_readed_list)

        elif user_input.lower() == "exit" or user_input.lower() == "quit":
            exit()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()

















