from django.urls import path
from pokemon import views

urlpatterns = [
    path('', views.home),
    # path('test', views.test_route),
    path('display', views.display_data, name='display'),
    path('localdata', views.local_data, name='localdata'),
    path('telephone', views.telephone, name='telephone'),
]
