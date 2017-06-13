from django.conf.urls import include, url

from .views import ListNamesView, ListNamesDelete, WinnerView

urlpatterns = [
    url(r'^$', ListNamesView.as_view(), name='list'),
    url(r'^winners/$', WinnerView.as_view(), name='winners'),
    url(r'^(?P<pk>\d+)/delete/$', ListNamesDelete.as_view(), name='delete'),
]
