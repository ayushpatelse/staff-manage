from django.urls import path,include
from . import views 
urlpatterns = [
    # path('',views.signOut,name="logout"),
    path('my_shifts/',views.my_shift,name="my_shifts"),
    path('shifts/',views.shift_list_view,name="shifts_all_view"),
    path('api-auth/', include('rest_framework.urls'))
]