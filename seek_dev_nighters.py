import requests
import json
from datetime import datetime 
from tzlocal import get_localzone
from pytz import timezone

def get_number_of_pages():
    r = requests.get('https://devman.org/api/challenges/solution_attempts/?page=2')
    j = json.loads(r.text)
    return j['number_of_pages']


def get_midnighters(pages):
    midnighters = set()

    for page in range(pages):
        r = requests.get( 'https://devman.org/api/challenges/solution_attempts/?page=' + str(page + 1) )
        j = json.loads(r.text)
        records = j["records"]

        for record in records:
            if record['timestamp'] is not None:
                username = record['username']
                timestamp = datetime.fromtimestamp(record['timestamp'])
                tz = record['timezone']

                client_time = timezone(tz).fromutc(timestamp)

                if 0 <= client_time.hour <= 4:
                    #print( username, client_time.hour)
                    midnighters.add(username)
    return midnighters     


if __name__ == '__main__':
    number_of_pages = get_number_of_pages()

    midnighters = get_midnighters(number_of_pages)

    for midnighter in midnighters:
        print(midnighter)