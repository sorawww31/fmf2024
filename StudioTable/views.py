from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import StudioTable, ReserveTable
from django.urls import reverse_lazy
# Create your views here.

class TableList(ListView):
    model = StudioTable
    context_object_name = "reserves"

class TableDetail(DetailView):
    model = StudioTable
    context_object_name = "reserve"

class ReserveCreate(CreateView):
    model = ReserveTable
    fields = "__all__"
    success_url = reverse_lazy("list")