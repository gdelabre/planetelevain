from django.conf.urls import url

from . import views

app_name = 'recettes'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<recipe_id>[0-9]+)/$', views.index, name='detail'),
]
