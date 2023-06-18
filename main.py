from termcolor import colored
from sys import platform
import configparser
import requests
import openai
import os


def clear():
	if platform == "linux" or platform == "linux2" or platform == "unix":
		os.system("clear")
	elif platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

colors = ['red', 'yellow', 'green', 'cyan', 'light_blue', 'magenta']
color_index = 0
bannercli ="""                                                   /$$                   /$$ /$$
                                                  |__/                  | $$|__/
  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$          /$$$$$$$| $$ /$$
 /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$ |____  $$| $$ /$$$$$$ /$$_____/| $$| $$
| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \ $$  /$$$$$$$| $$|______/| $$      | $$| $$
| $$  | $$| $$  | $$| $$_____/| $$  | $$ /$$__  $$| $$        | $$      | $$| $$
|  $$$$$$/| $$$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$        |  $$$$$$$| $$| $$
 \______/ | $$____/  \_______/|__/  |__/ \_______/|__/         \_______/|__/|__/
          | $$                                                                  
          | $$                                                                  
          |__/    """

def banner():
    for i in range(len(bannercli)):
        color = colors[i % len(colors)]
        print(colored(bannercli[i], color), end="")
    print(colored("\n\nAuthor: ", "red") + "@avencores")
    print(colored("Telegram channel: ", "red") + "@hzfnews")

clear()
banner()  
config = configparser.ConfigParser()
config.read('config.ini')
if 'openai-token' not in config:
    token = input(colored("\nEnter your token ", "yellow") + colored(">> ", "green"))
    config['openai-token'] = {'token': token}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
        clear()
        print(colored("Please reload this application!", "cyan"))
        exit()
else:
    token = config['openai-token']['token']

def menu():
    while True:
        openai.api_key = token
        clear()
        banner()
        print(colored("\n[1] ", "cyan") + "ChatGPT")
        print(colored("[2] ", "cyan") + "DALLE-2")
        print(colored("[3] ", "cyan") + "Whisper")
        print(colored("\n[4] ", "cyan") + "Change openai token")
        print(colored("[5] ", "cyan") + "Change openai session key")
        print(colored("\n[6] ", "cyan") + "Check token balance")
        print(colored("\n[0] ", "cyan") + "Exit")
        choice = input(colored("\nEnter your choice (0-6) ", "yellow") + colored(">> ", "green"))
        if choice == "0":
            clear()
            print(colored("Bye!", "cyan"))
            exit()
        if choice == "1":
            clear()
            banner()
            print(colored("\n[1] ", "cyan") + "ChatGPT 4.0 (32K)")
            print(colored("[2] ", "cyan") + "ChatGPT 4.0")
            print(colored("[3] ", "cyan") + "ChatGPT 3.5 (16K)")
            print(colored("[4] ", "cyan") + "ChatGPT 3.5")
            choice = input(colored("\nEnter your choice (1-4) ", "yellow") + colored(">> ", "green"))
            if choice == "1":
                clear()
                banner()
                print(colored("\nChatGPT Model: ", "light_blue") + "4.0 (32K)")
                resp = input(colored("\nEnter your request (leave blank to keep existing) ", "yellow") + colored(">> ", "green"))
                if resp:
                    try:
                        response = openai.ChatCompletion.create(
                        model="gpt-4-32k",
                        messages=[{"role": "user", "content": resp}])
                        output = response["choices"][0]["message"]["content"]
                        print(colored(f"\nResponse from ChatGPT 4.0 (32K) ", "magenta") + colored(">> ", "green") + output)
                        print(colored("\nPress ENTER to return to the main menu", "cyan"))
                        input()
                    except Exception as e:
                        clear()
                        banner()
                        print(colored("\nERROR ", "yellow") + colored(">> ", "green")) + str(e)
                        print(colored("\nPress ENTER to return to the main menu", "cyan"))
                        input()
                        menu()
                else:
                    menu()
            if choice == "2":
                clear()
                banner()
                print(colored("\nChatGPT Model: ", "light_blue") + "4.0")
                resp = input(colored("\nEnter your request (leave blank to keep existing) ", "yellow") + colored(">> ", "green"))
                if resp:
                    try:
                        response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": resp}])
                        output = response["choices"][0]["message"]["content"]
                        print(colored(f"\nResponse from ChatGPT 4.0 ", "magenta") + colored(">> ", "green") + output)
                        print(colored("\nPress ENTER to return to the main menu", "cyan"))
                        input()
                    except Exception as e:
                        clear()
                        banner()
                        print(colored("\nERROR ", "yellow") + colored(">> ", "green")) + str(e)
                        print(colored("\nPress ENTER to return to the main menu", "cyan"))
                        input()
                        menu()
                else:
                    menu()
            if choice == "3":
                clear()
                banner()
                print(colored("\nChatGPT Model: ", "light_blue") + "3.5 (16K)")
                resp = input(colored("\nEnter your request (leave blank to keep existing) ", "yellow") + colored(">> ", "green"))
                if resp:
                    try:
                        response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo-16k",
                        messages=[{"role": "user", "content": resp}])
                        output = response["choices"][0]["message"]["content"]
                        print(colored(f"\nResponse from ChatGPT 3.5 (16K) ", "magenta") + colored(">> ", "green") + output)
                        print(colored("\nPress ENTER to return to the main menu", "cyan"))
                        input()
                    except Exception as e:
                        clear()
                        banner()
                        print(colored("\nERROR ", "yellow") + colored(">> ", "green")) + str(e)
                        print(colored("\nPress ENTER to return to the main menu", "cyan"))
                        input()
                        menu()
                else:
                    menu()
            if choice == "4":
                clear()
                banner()
                print(colored("\nChatGPT Model: ", "light_blue") + "3.5")
                resp = input(colored("\nEnter your request (leave blank to keep existing) ", "yellow") + colored(">> ", "green"))
                if resp:
                    try:
                        response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": resp}])
                        output = response["choices"][0]["message"]["content"]
                        print(colored(f"\nResponse from ChatGPT 3.5 ", "magenta") + colored(">> ", "green") + output)
                        print(colored("\nPress ENTER to return to the main menu", "cyan"))
                        input()
                    except Exception as e:
                        clear()
                        banner()
                        print(colored("\nERROR ", "yellow") + colored(">> ", "green")) + str(e)
                        print(colored("\nPress ENTER to return to the main menu", "cyan"))
                        input()
                        menu()
                else:
                    menu()
            else:
                clear()
                banner()
                print(colored("\nInvalid choice. Please try again.", "light_blue"))
                print(colored("\nPress ENTER to return to the main menu", "cyan"))
                input()
        elif choice == "2":
            clear()
            banner()
            resp = input(colored("\nEnter your request (leave blank to keep existing) ", "yellow") + colored(">> ", "green"))
            if resp:
                try:
                    response = openai.Image.create(
                        prompt=resp,
                        n=1,
                        size="1024x1024")
                    output = response['data'][0]['url']
                    print(colored(f"\nResponse from DALLE-2 ", "magenta")  + colored(">> ", "green") + output)
                    print(colored("\nPress ENTER to return to the main menu", "cyan"))
                    input()
                except Exception as e:
                    clear()
                    banner()
                    print(colored("\nERROR ", "yellow") + colored(">> ", "green")) + str(e)
                    print(colored("\nPress ENTER to return to the main menu", "cyan"))
                    input()
                    menu()
        elif choice == "3":
            clear()
            banner()
            print(colored("\nFile uploads are currently limited to 25 MB and the following input file types are supported: mp3, mp4, mpeg, mpga, m4a, wav, and webm.", "green"))
            resp = input(colored("\nEnter the full path to the file (leave blank to keep existing) ", "yellow") + colored(">> ", "green"))
            if resp:
                try:
                    fileaudio = open(f"{resp}", "rb")
                    response = openai.Audio.transcribe("whisper-1", fileaudio)
                    fileaudio.close()
                    output = response["text"]
                    print(colored(f"\nResponse from Whisper ", "magenta")  + colored(">> ", "green") + output)
                    print(colored("\nPress ENTER to return to the main menu", "cyan"))
                    input()
                except Exception as e:
                    clear()
                    banner()
                    print(colored("\nERROR ", "yellow") + colored(">> ", "green")) + str(e)
                    print(colored("\nPress ENTER to return to the main menu", "cyan"))
                    input()
                    menu()
        elif choice == "4":
            clear()
            banner()
            new_token = input(colored("\nEnter new token (leave blank to keep existing) ", "yellow") + colored(">> ", "green"))
            if new_token:
                config['openai-token']['token'] = new_token
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
                    clear()
                    print(colored("Please reload this application!", "cyan"))
                    exit()
        elif choice == "5":
            clear()
            banner()
            print(colored("\nRead this article: ", "light_blue") + "https://lmmsoft.github.io/openai_update_check_balance_api/")
            session_key = input(colored("\nEnter your session-key (leave blank to keep existing) ", "yellow") + colored(">> ", "green"))
            if session_key:
                config['openai-key'] = {'session_key': session_key}
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
                    clear()
                    print(colored("Please reload this application!", "cyan"))
                    exit()
        elif choice == "6":
            clear()
            banner()
            try:
                if 'openai-key' not in config:
                    clear()
                    banner()
                    print(colored("\nRead this article: ", "light_blue") + "https://lmmsoft.github.io/openai_update_check_balance_api/")
                    session_key = input(colored("\nEnter your session-key ", "yellow") + colored(">> ", "green"))
                    config['openai-key'] = {'session_key': session_key}
                    with open('config.ini', 'w') as configfile:
                        config.write(configfile)
                        clear()
                        print(colored("Please reload this application!", "cyan"))
                        exit()
                else:
                    session_key = config['openai-key']['session_key']
                url = "https://api.openai.com/dashboard/billing/credit_grants"
                headers = {
                    "Content-Type": "application/json",
                    f"Authorization": f"Bearer {session_key}"
                }

                response = requests.get(url, headers=headers)
                data = response.json()
                balance = data['total_used']
                totalbalance = data['total_granted']
                totalavailable = data['total_available']
                print(colored("\nTotal token balance: ", "yellow") + str(totalbalance))
                print(colored("Used token balance: ", "yellow") + str(balance))
                print(colored("Total balance of token: ", "yellow") + str(totalavailable))
                print(colored("\nPress ENTER to return to the main menu", "cyan"))
                input()
            except Exception as e:
                clear()
                banner()
                print(colored("\nERROR ", "yellow") + colored(">> ", "green")) + str(e)
                print(colored("\nPress ENTER to return to the main menu", "cyan"))
                input()
                menu()
        else:
            clear()
            banner()
            print(colored("\nInvalid choice. Please try again.", "light_blue"))
            print(colored("\nPress ENTER to return to the main menu", "cyan"))
            input()

menu()