
from django.conf.urls import url
import views
from django.views.static import serve
from the_taz.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^/$', views.post_list),
    url(r'^/(?P<id>\d+)/$', views.post_detail),
    url(r'^/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

]