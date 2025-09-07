from django.shortcuts import render,redirect
from .models import Shift
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.db.models import Q
import time
# Create your views here.

@login_required
def my_shift(request):
    shift_list = Shift.objects.filter(assigned_employee__user=request.user)
    return render(request,'scheduling/my_shifts.html',{"shift_list":shift_list})

@login_required
@user_passes_test(lambda u:u.groups.filter(name="Managers").exists())
def shift_list_view(request):
    
    shifts = Shift.objects.all()

    # Filter Logic
    status_selected = [ status  for status,text in Shift.SHIFT_STATUS if request.GET.get(status) ]
    print(status_selected)

    if status_selected:
        status_query = Q()
        for s in status_selected:
            print(s)
            status_query |= Q(status=s)
        shifts = shifts.filter(status_query)
        print(shifts)


    return render(request,'scheduling/shifts_all.html',{"shift_list":shifts})

        