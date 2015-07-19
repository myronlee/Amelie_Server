from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Emilie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^searchSimilarImages/$', views.search_similar_images),
    url(r'^Images/(.*)/$', views.get_similar_image),
    url(r'^protocol/$', views.get_protocol),
    url(r'^license/$', views.get_liscense),
    url(r'^FAQ/$', views.get_faq),
    url(r'^about/$', views.get_about),

    url(r'^admin/', include(admin.site.urls)),
)
