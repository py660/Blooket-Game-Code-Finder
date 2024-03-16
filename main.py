# CONFIG AREA BELOW
useWebhook = False # Use a discord webhook or not, if yes, fill in the line below
webhook = 'Your discord webhook url'
thread_amount = 25 # How many threads to use? Put it below 10 if using on your home computer. 25 max (also fastest)
logInvalids = False # Don't enable unless you want to have your console spammed (does not send to discord)
# Config area end, do not edit below code

#from discord_webhook import DiscordWebhook

import random
import requests
import threading
import os
bsid = os.environ["BSID"] #YOUR BSID HERE

def main():
    while 1:
        while True:
            random_numbers = str(random.randint(1000000, 9999999))
            try:
                response = requests.get(
                    f"https://fb.blooket.com/c/firebase/id?id={random_numbers}",
                    cookies={"bsid": bsid})
                while response.status_code == 429:
                    response = requests.get(
                    f"https://fb.blooket.com/c/firebase/id?id={random_numbers}",
                    cookies={"bsid": bsid})
                if response.json()["success"]:
                    print("Valid Game Code:", random_numbers)
                else:
                    pass
                    #print("Nope")
                #data = response.json()
            except Exception as e:
                print('Something went wrong: '+e)


if __name__ == "__main__":
    try:
        threads = list()

        for index in range(thread_amount):
            _ = threading.Thread(target=main)

            threads.append(_)

            _.start()

        for index, thread in enumerate(threads):
            thread.join()
    except KeyboardInterrupt:
        exit()