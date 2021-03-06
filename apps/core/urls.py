from django.conf.urls import patterns, include, url
import views
from tastypie.api import Api
import api

v1_api = Api(api_name='1')
v1_api.register(api.UserResource())
v1_api.register(api.ContainerResource())
v1_api.register(api.ObjectResource())


urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view()),
    url(r'^api/', include(v1_api.urls)),
)
