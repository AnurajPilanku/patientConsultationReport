from django.urls import path


from . import views
urlpatterns=[
    # path('index', views.index,name='index'),
    # path('about', views.about,name='about'),
    path('add', views.consultation, name='consultation')
]


#when first parameter inside path is added to the host , then it will execute the  function inside view.py eg-- http://127.0.0.1:8000/index, http://127.0.0.1:8000//consult
