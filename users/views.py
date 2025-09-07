from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Q

# Self Created
from .forms import RegisterUserForm,LoginForm,UserEditForm,EmployeeEditForm,ManagerEmployeeEditForm
from .models import Employee,CustomUser

# Create your views here.

@login_required
def home(request):

    return render(request,"users/home.html")

def register(request):
    if request.method=="POST":
        registerForm = RegisterUserForm(request.POST)
        print(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            print("registeration successfull")
            # return redirect("signIn")
        else:
            print("Registeration failed")
            print(registerForm.errors.as_json())
    else:
        registerForm = RegisterUserForm()

    return render(request,"users/register.html",{"form":registerForm})


def signOut(request):
    logout(request)

    return redirect("signIn")


def signIn(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            sec_id = form.cleaned_data['sec_id']
            password = form.cleaned_data['password']
            print("Sec ID:",sec_id, "  pass:",password)
            UserModel = get_user_model() 
            if UserModel :

                user = authenticate(request,**{UserModel.USERNAME_FIELD:sec_id},password=password)
                print(user)
                if user is not None:
                    messages.success(request,"Login Successfull!")
                    login(request,user)
                    return redirect("scheduling_home")
                messages.error(request,"Login Unsuccessfull!")
                print("*******UserModel not found*******")
    else:
        form = LoginForm()
    return render(request,"users/login.html",{"form":form})

@login_required
def profile_view(request,pk):
    print(pk)
    try:
        instance = Employee.objects.get(user__sec_id=pk)
        print(instance.date_join)
        return render(request,'users/profile.html',{"user":instance})
    except Employee.DoesNotExist:
        print(f"ERROR: Employee profile not found for CustomUser with sec_id '{pk}'.")
        return redirect("scheduling_home") # Or render a specific 'profile not found' template

    except ValueError as e:
        print(f"ERROR: ValueError during lookup (e.g., pk type issue): {e}")
        return redirect("scheduling_home")
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return redirect("scheduling_home")

@login_required
def profile_edit(request,pk):
    try:
        user = CustomUser.objects.get(sec_id=pk)
        emp_profile = get_object_or_404(Employee,user=user) 
        
        if request.method =="POST":
            user_form = UserEditForm(request.POST,instance=user)
            employee_form = EmployeeEditForm(request.POST ,instance=emp_profile)
 
            
            if user_form.is_valid() and employee_form.is_valid():
                user_form.save()
                employee_form.save()
                messages.success(request,f"Profile of {user.first_name} {user.last_name} has been changed successfully!")
                return redirect("profile_view",pk=user.sec_id)
        
        else:
            user_form = UserEditForm(instance=user)
            employee_form = EmployeeEditForm(instance=emp_profile)
        
        return render(request,'users/profile_edit.html',{'user_form':user_form,"emp_form":employee_form})
    
    except Employee.DoesNotExist:
        print(f"ERROR: Employee profile not found for CustomUser with sec_id '{pk}'.")
        return redirect("scheduling_home")

    except ValueError as e:
        print(f"ERROR: ValueError during lookup (e.g., pk type issue): {e}")
        return redirect("scheduling_home")
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")
        return redirect("scheduling_home")

# Manager/Admin Features


@login_required
@permission_required('users.can_manage')
def employee_list(request):
    emp_list = Employee.objects.all().exclude(role="MR").select_related("user")
    query = request.GET.get('q')
    

    if query:
        emp_list = emp_list.filter(
            Q(user__sec_id__icontains=query),
            Q(user__first_name__icontains=query),
            Q(user__last_name__icontains=query),
            Q(user__email__icontains=query),
        )
    
    return render(request,'users/employee_list.html',{"emp_list":emp_list})

@login_required
@permission_required('users.can_manage')
def employee_view(request,pk):
    try:
        employee = Employee.objects.get(user__sec_id=pk)
    except Employee.DoesNotExist:
        print(f" Employee with Sec ID:{pk} does not exist!")
        messages.error(request,"Employee Edit Could not be found")
    except Exception as e:
        print("Error! - ",e)
        messages.error(request,"Error - Employee Edit")
        return redirect("scheduling_home")
    
    return render(request,'users/employee_view.html',{"employee":employee})


@login_required
@permission_required('users.can_manage')
def employee_edit(request,pk):
    try:
        employee = Employee.objects.get(user__sec_id=pk)
        
        if request.method =="POST":
            user_form = UserEditForm(request.POST,instance=employee.user)
            emp_form = ManagerEmployeeEditForm(request.POST,instance=employee)
            if user_form.is_valid() and emp_form.is_valid():
                user_form.save()
                emp_form.save()
                return redirect("employee_view",pk=employee.user.sec_id)
        else:
            user_form = UserEditForm(instance=employee.user)
            emp_form = ManagerEmployeeEditForm(instance=employee)
        

    except Employee.DoesNotExist:
        print(f" Employee with Sec ID:{pk} does not exist!")
        messages.error(request,"Employee Edit Could not be found")
    except Exception as e:
        print("Error! - ",e)
        messages.error(request,"Error - Employee Edit")
        return redirect("scheduling_home")
    
    return render(request,'users/employee_edit.html',{"emp_form":emp_form,"user_form":user_form,"obj":employee})


