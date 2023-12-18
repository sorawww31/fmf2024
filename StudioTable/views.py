from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import StudioTable
# Create your views here.

class TableList(ListView):
    model = StudioTable
    context_object_name = "reserves"

class TableDetail(DetailView):
    model = StudioTable
    context_object_name = "reserve"