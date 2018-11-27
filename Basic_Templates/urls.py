from django.urls import path
from Basic_Templates import views

#TEMPLATE TAGGING
app_name ='Basic_Templates'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
 ]

