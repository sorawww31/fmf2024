from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import StudioTable, ReserveTable
from django.db.models import Q
from django.urls import reverse_lazy
# Create your views here.

class TableList(ListView):
    model = StudioTable
    contect_object_name = "studio_table"


class WeekList(ListView):
    model = StudioTable
    def get_queryset(self):
        #return StudioTable.objects.filter(ExtractWeekDay('date')==1)  # 月曜日だけを表示
        return StudioTable.objects.filter(date__week_day=2, period = '1限').order_by('date')[0:3]
    context_object_name = "mondays"

class TableDetail(DetailView):
    model = StudioTable
    context_object_name = "reserve"

def day_and_period(request):
    period = ['1限','2限','昼休み','3限','4限','5限','6限','7限']

class ReserveCreate(CreateView):
    model = ReserveTable
    fields = "__all__"
    success_url = reverse_lazy("list")