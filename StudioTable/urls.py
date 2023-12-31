from django.urls import path
from .views import TableList, ReserveCreate, TableDetail, WeekList

urlpatterns = [
    path("", WeekList.as_view(), name="week"),
    path("table/<int:pk>", TableList.as_view() , name = "table"),
    path("detail/<int:pk>", TableDetail.as_view(), name="detail"),
    path("create/", ReserveCreate.as_view(), name="create"),
]