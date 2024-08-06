from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('create/',views.create_task, name='create'),
    path('delete/<int:pk>',views.delete_task, name='delete'),
    path('update/<int:pk>',views.update_task, name='update'),
    path('finished/',views.finished_tasks, name='finished')
]
