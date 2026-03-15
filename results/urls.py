from django.urls import path
from . import views

urlpatterns = [
    path('',               views.dashboard,      name='dashboard'),
    path('login/',         views.login_view,      name='login'),
    path('logout/',        views.logout_view,     name='logout'),
    path('students/',      views.student_list,    name='student_list'),
    path('students/add/',  views.student_add,     name='student_add'),
    path('students/<int:pk>/edit/',   views.student_edit,   name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('results/',       views.result_list,     name='result_list'),
    path('results/add/',   views.result_add,      name='result_add'),
    path('results/<int:pk>/delete/', views.result_delete, name='result_delete'),
    path('view-result/',   views.view_result,     name='view_result'),
]
