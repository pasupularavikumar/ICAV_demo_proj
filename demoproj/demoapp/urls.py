from django.urls import path
from .import views 
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router =DefaultRouter()
router.register('book_api',views.bookviewset,basename='book')


urlpatterns =[

    path('', views.home,name='home'),
    path('addbook/',views.addbook,name='addbook'),
    path('updatebook/<int:id>/',views.updatebook,name='updatebook'),
    path('login', views.login,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('',include(router.urls)),

]