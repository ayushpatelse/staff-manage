from django.urls import path
from . import views 
urlpatterns = [
    path('home',views.home,name="scheduling_home"),
    path('signIn',views.signIn,name="signIn"),
    path('register',views.register,name="register"),
    path('logout',views.signOut,name="logout"),
    path('profile_view/<int:pk>',views.profile_view,name="profile_view"),
    path('profile_edit/<int:pk>',views.profile_edit,name="profile_edit"),
    
    # Employee Urls
    path('employee_list/',views.employee_list,name="employee_list"),
    path('employee_view/<int:pk>',views.employee_view,name="employee_view"),
    path('employee_edit/<int:pk>',views.employee_edit,name="employee_edit"),
    
]