from django.urls import path
from .api import GetStories

urlpatterns = [
	path('get-stories/', GetStories.as_view()),
]