from django.urls import path
from .views import TableList

urlpatterns = [
    path("", TableList.as_view(), name="list"),
]