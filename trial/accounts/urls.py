from django.urls import path
from  .views import *


urlpatterns=[
    path('register',registerpage,name='register'),
    path('login',loginpage,name='login'),
    path('<int:id>',home,name='home'),
    path('addwebsite/<int:id>/',addWebsite,name='addWebsite'),
    path('search/<int:id>/',search,name='search'),
    path('contact/<int:id>/',contact,name='contact'),
    path('profile/<int:id>/',profile,name='profile'),
    path('update/<int:id>/',updatewebsite,name='update'),
    path('delete/<int:id>/',deletewebsite,name='delete'),
    path('',index,name='index')
]
