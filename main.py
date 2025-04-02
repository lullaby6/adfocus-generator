import requests, os
from dotenv import load_dotenv
from pyperclip import copy

load_dotenv()

api_key = os.getenv("API_KEY")

os.system("title AdFocus Generator")

while True:
    try:
        os.system("cls")

        url = input("URL: ")

        endpoint = f"http://adfoc.us/api/?key={api_key}&url={url}"

        response = requests.get(endpoint)

        print("")
        print(response.text)

        copy(response.text)

        print("")
        print("Copied to clipboard")

        print("")
        input("Press enter to continue...")
    except Exception as e:
        input(e)