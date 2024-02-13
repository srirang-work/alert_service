from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('alerts/create/', views.AlertCreateView.as_view(), name='alert-create'),
    path('alerts/delete/<int:pk>/', views.AlertDeleteView.as_view(), name='alert-delete'),
    path('alerts/', views.AlertListView.as_view(), name='alert-list'),
    path('signup/', views.UserSignupView.as_view(), name='user-signup'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
]
