from django.conf.urls import include, url
from find import views
urlpatterns = [
    url(r'^$', include('find.urls', namespace="find")),
    url(r'^bars\/(?P<location>/*.+)$',
        views.get_drunk, name='bars'),
    url(r'^cafe\/(?P<location>/*.+)$',
        views.get_cafes, name='cafe'),
    url(r'^party\/(?P<location>/*.+)$',
        views.get_parties, name='party'),
    url(r'^wronglocation$',
        views.wrong_location, name='wrong_location'),


]
