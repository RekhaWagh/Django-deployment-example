from django.contrib import admin
from django.urls import path
from basic_app import views
urlpatterns = [
   
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('other',views.other,name='other'),
    path('relative',views.relative,name='relative'),
]