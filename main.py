
#from discord_webhook import DiscordWebhook

import random
import requests
import threading
import os
def genBSID():
    sess = requests.Session()
    sess.get("https://play.blooket.com/play")
    return sess.cookies["bsid"]
webhook = os.environ.get("WEBHOOK") #YOUR WEBHOOK URL HERE
thread_amount = int(os.environ["THREADS"]) if os.environ.get("THREADS") else 25 # How many threads to use? Put it below 10 if using on your home computer. 25 max (also fastest)


def main():
    bsid = [genBSID() for i in range(10)]
    while True:
        random_numbers = str(random.randint(1000000, 9999999))
        try:
            response = requests.get(
                f"https://fb.blooket.com/c/firebase/id?id={random_numbers}",
                cookies={"bsid": bsid[random.randint(0,9)]})
            while response.status_code == 429:
                response = requests.get(
                f"https://fb.blooket.com/c/firebase/id?id={random_numbers}",
                cookies={"bsid": bsid[random.randint(0,9)]})
            if response.status_code == 403:
                bsid = [genBSID() for i in range(10)]
            if response.json()["success"]:
                print("Valid Game Code:", random_numbers)
                if webhook:
                    requests.post(webhook, json={"content": f"Game Code Found: {random_numbers}\t - [Join](<https://play.blooket.com/play?id={random_numbers}>)"})
            else:
                pass
                #print("Nope")
            #data = response.json()
        except Exception as e:
            print('Something went wrong:')
            print(e)


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