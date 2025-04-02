import requests, os
from dotenv import load_dotenv
from pyperclip import copy

def main():
    os.system("title AdFocus Generator")

    load_dotenv()

    api_key = os.getenv("API_KEY")

    while True:
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

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
            input(e)