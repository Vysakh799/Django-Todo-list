from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('update/<pk>',views.update),
    path('delete/<pk>',views.delete)

]