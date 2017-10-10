from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'col_list/', col_list, name='col_list'),
    url(r'college/(?P<col_id>\d+)/$', col_submit, name='col_submit'),
]