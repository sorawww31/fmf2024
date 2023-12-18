from django.urls import path
from .views import TableList, ReserveCreate, TableDetail

urlpatterns = [
    path("", TableList.as_view(), name="list"),
    path("detail/<int:pk>", TableDetail.as_view(), name="detail"),
    path("create/", ReserveCreate.as_view(), name="create")
]