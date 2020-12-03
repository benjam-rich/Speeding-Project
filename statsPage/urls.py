from django.urls import path
from .views import statsPageView, enterDataPageView, storeDriverPageView

urlpatterns = [
    path("enterdata/", enterDataPageView, name="enterData"),
    path("storeDriver/", storeDriverPageView, name="storeDriver"),
    path("display/", statsPageView, name="display")
]
