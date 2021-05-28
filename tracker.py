import os
import re

import feedparser
import paho.mqtt.publish as publish
from dotenv import load_dotenv

# .env file
load_dotenv()

auth = {'username':os.getenv("USERNAME"), 'password': os.getenv("PASSWORD")}

def update_year(value):
    # TODO TLS support inbouwen
    publish.single(payload=value, topic=os.getenv("TOPIC"), hostname=os.getenv("BROKER"), tls=None, auth=auth)

def rss_checker():
    rss_feed = feedparser.parse("https://www.rivm.nl/nieuws/rss.xml")

    for message in rss_feed.entries:
        # Pak datum uit titel als
        # "(...) 19XX uitgenodigd voor coronavaccinatie"
        regex = re.findall(r"(\b19[0-9]{2})(?=\suitgenodigd)", message.title)

        if len(regex) > 0:
            # Alleen eerste resultaat nodig
            rss_year = int(regex[0])

            # Update met laatste waarde en stop
            update_year(rss_year)
            break

if __name__ == '__main__':
    rss_checker()