from rest_framework.views import APIView
from rest_framework.response import Response
import json

from .methods import get_login_session
from .methods import fetch_stories

class GetStories(APIView):

    def get(self, request, format = None):

        cookie = request.META['HTTP_AUTHORIZATION']
        session = get_login_session(cookie)

        response = session.get("https://i.instagram.com/api/v1/feed/reels_tray/")
        responseobj = json.loads(response.text)
        ids = []
        if response.status_code == 200:
            for item in responseobj['tray']:
                ids.append([str(item['id']),item['user']['full_name']])
        else:
            ids.append('null')
        print(ids)
        response = fetch_stories(ids,session)

        return Response(response)