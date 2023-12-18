from django.urls import path
from .views import TableList, DetailView, TableDetail

urlpatterns = [
    path("", TableList.as_view(), name="list"),
    path("detail/<int:pk>", TableDetail.as_view(), name="detail"),
]