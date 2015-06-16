#import django_cron 
#django_cron.autodiscover()

from django.conf.urls import patterns, include, url
from ask_lantratov.views import hello
from ask.views import index, ask, answer, login, logout, register, none_answer, settings, ques_answer_vote, right_answer
#from ask.views import index_temp 
#from ask.views import home, home2
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_lantratov.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	#url(r'^blog/', include('ask.urls')),

    #url(r'^home/$', home, name = 'home'),
    #url(r'^home2/(\d+)/$', home2, name = 'home2'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello$', hello, name = 'hello'),

    url(r'^$', index, name = 'index'),
    #url(r'^$', index_temp, name = 'index'),
    url(r'^ask/$', ask, name = 'ask'),
    url(r'^answer/(\d+)/$', answer, name = 'answer'),
    url(r'^ques_answer/vote/$', ques_answer_vote, name = 'ques_answer_vote'),
    url(r'^right_answer/$', right_answer, name = 'right_answer'),
    url(r'^answer/$', none_answer, name = 'none_answer'),
    url(r'^login/$', login, name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^register/$', register, name = 'register'),
    url(r'^settings/$', settings, name = 'settigns')
)
