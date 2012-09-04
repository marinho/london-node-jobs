from london.urls.defining import patterns, include
from london.conf import settings

url_patterns = patterns('jobs.views',
    ('^$', 'jobs_get'),
    ('^post/$', 'jobs_post'),
    ('^delete/$', 'jobs_delete'),
    ('^next/$', 'jobs_get_next'),
    ('^expire/$', 'jobs_expire'),
    ('^(?P<id>\w+)/update/$', 'jobs_update'),
)

