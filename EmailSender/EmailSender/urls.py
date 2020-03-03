from django.contrib import admin
from django.urls import path
from emailapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact',views.form_process_view,name='contact'),
    path('',views.home,name='home'),
    path('map',views.map,name='map')
]
