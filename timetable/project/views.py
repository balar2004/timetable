from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
# Create your views here.

def timetable(request):
    return render(request,"html/timetable.html")