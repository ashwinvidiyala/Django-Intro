from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.session_words),
    url(r'^session_words$', views.session_words),
    url(r'^session_words/add', views.add),
    url(r'^session_words/delete', views.delete),
]
