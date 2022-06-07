from django.contrib import admin
from django.urls import path, include
from app import views
from app import api_views
from rest_framework import routers

from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register('api/ariza', api_views.arizaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('ariza/', views.arizaPage, name='ariza'),
    path('index/', views.indexPage, name='index'),
    path('about/', views.aboutPage, name='about'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # custom APIs
    path('api/get-by-pinfl/', api_views.GetByPINFL.as_view(), name="get_by_pinfl"),
]