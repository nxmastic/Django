from django.urls import path, include
from.import views

urlpatterns = [
    # path('',views.LoginForm.as_view(), name='Login')
    path('register',views.register, name='register'),
]

