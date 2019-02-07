import requests
import json

def get_login_session(cred):
    session = requests.Session()
    session.headers['user-agent'] = "Instagram 10.3.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+"
    session.headers.update({'cookie': cred})
    session.headers["x-ig-capabilities"] = "36oD"
    session.headers["cache-control"] = "no-cache"
    return session

def fetch_stories(ids, session):
    urls = {}
    urls['pic_urls'] = []
    urls['usernames'] = []
    for user in ids:
        urls['pic_urls'].append(userid[2])
        urls['usernames'].append(userid[3])
    for userid in ids:
        urls[userid[1]]=[]
        response = session.get("https://i.instagram.com/api/v1/feed/user/"+ userid[0] +"/reel_media/")
        responseobj = json.loads(response.text)
        if response.status_code == 200:
            for item in responseobj['items']:
                id = item['id']
                try:
                    url = item['video_versions'][0]['url']
                    urls[userid[1]].append(url)
                except KeyError: #if there are no videos of this item
                    url = item['image_versions2']['candidates'][0]['url']
                    urls[userid[1]].append(url)
    return urls