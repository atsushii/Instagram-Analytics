from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('log_in/', views.LogInView.as_view(), name='log_in'),
    path('update/', views.ManageUserView.as_view(), name='update'),
]
