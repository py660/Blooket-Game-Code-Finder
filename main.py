
#from discord_webhook import DiscordWebhook

import random
import requests
import threading
import os
def genBSID():
    sess = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    sess.get("https://play.blooket.com/play", headers=headers)
    return sess.cookies["bsid"]
webhook = os.environ.get("WEBHOOK") #YOUR WEBHOOK URL HERE
thread_amount = int(os.environ["THREADS"]) if os.environ.get("THREADS") else 25 # How many threads to use? Put it below 10 if using on your home computer. 25 max (also fastest)


def main():
    bsid = [genBSID() for i in range(10)]
    while True:
        random_numbers = str(random.randint(1000000, 9999999))
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            response = requests.get(
                f"https://fb.blooket.com/c/firebase/id?id={random_numbers}",
                cookies={"bsid": bsid[random.randint(0,9)]}, headers=headers)
            while response.status_code == 429:
                response = requests.get(
                f"https://fb.blooket.com/c/firebase/id?id={random_numbers}",
                cookies={"bsid": bsid[random.randint(0,9)]}, headers=headers)
            if response.status_code == 403:
                bsid = [genBSID() for i in range(10)]
            elif response.json()["success"]:
                print("Valid Game Code:", random_numbers)
                if webhook:
                    requests.post(webhook, json={"content": f"Game Code Found: [Join](<https://play.blooket.com/play?id={random_numbers}>) - {random_numbers}"})
            else:
                pass
                #print("Nope")
            #data = response.json()
        except KeyboardInterrupt as e:
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