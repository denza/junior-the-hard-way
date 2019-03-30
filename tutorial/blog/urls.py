from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    #home page
    path('', views.IndexView.as_view(), name = "index"),
    #detail page
    path('blog/<pk>', views.DetailView.as_view(), name="detail"),
]