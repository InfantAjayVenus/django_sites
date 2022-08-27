from django.urls import include, path
from . import views

app_name = 'short_urls'
urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add_url, name="add"),
    path('url-list', views.url_list, name="list"),
    path('account', include('django.contrib.auth.urls')),
    path('<str:slug>', views.go_to_page, name='goto'),
]
