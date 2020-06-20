from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('analyze',views.analyze,name='analyze'),
    path('',views.index2,name='index2'),
]




