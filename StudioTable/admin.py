from django.contrib import admin
from .models import StudioTable,ReserveTable
import datetime
from django.shortcuts import redirect
from django.urls import path
# Register your models here.
admin.site.register(ReserveTable)

@admin.register(StudioTable)
class StudioTableAdmin(admin.ModelAdmin):
    actions = ['create_weekly_schedule']
    def create_weekly_schedule(self, request, queryset):
        date_offset = queryset[0].date
        print(f"{date_offset}")
        for day in range(7):
            for period in ('1限', '2限', '昼休み', '3限', '4限', '5限', '6限', '7限'):
                StudioTable.objects.create(date = date_offset + datetime.timedelta(days=day), period=period)
        queryset.delete()
        return redirect('/admin/StudioTable/studiotable/')
