from django.urls import path

from . import views

urlpatterns = [
    path('', views.card_index, name='card_index'),
    path("<int:pk>/", views.card_detail, name="card_detail"),
]