from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.LoginUser,name='login'),
    path('logout',views.LogoutUser,name='logout'),
    path('add_emp',login_required(views.add_emp),name='add_emp'),
    path('all_emp',login_required(views.all_emp),name='all_emp'),
    path('remove_emp',login_required(views.remove_emp), name="remove_emp"),
    path('remove_emp/<int:emp_id>',views.remove_emp,name="remove_emp"),
    path('filter_emp',login_required(views.filter_emp),name='filter_emp'),
    path('about', login_required(views.about), name='about')

]
