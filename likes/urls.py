from django.conf.urls import patterns, include, url
from django.contrib import admin

from principal.views import IndexView, LikeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'likes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', IndexView.as_view()),
    url(r'^like/$', LikeView.as_view()),
    
    url(r'^dando-like$', 'principal.views.dandolike'),
    url(r'^admin/', include(admin.site.urls)),
)
