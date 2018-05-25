from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addWish, name='add'),
    path('complete/<wish_id>', views.completeWish, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]
