from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership_form, name='membership_form'),
    path('receipt/<int:member_id>/', views.membership_receipt, name='membership_receipt'),
]