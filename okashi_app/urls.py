from django.urls import path
from . import views

app_name='okashi_app'
urlpatterns=[
        path('',views.index,name='index'),
        path("question",views.question,name="question"),
        path("recommend",views.recommend,name="recommend"),
]
