from django.urls import path
from .views import HomePageView
urlpatterns=[

    path("post/",HomePageView.as_view())
]