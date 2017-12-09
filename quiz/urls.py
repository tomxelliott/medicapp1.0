from django.conf.urls import url

from . import core_views
from . import quiz_views

app_name = 'quiz'
urlpatterns = [
    url(r'^$', quiz_views.index, name='index'),
    url(r'^(?P<topic_id>[0-9]+)/question/$', quiz_views.question, name='question'),
    url(r'^(?P<question_id>[0-9]+)/$', quiz_views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/answer/$', quiz_views.answer, name='answer'),
    url(r'^out_of_questions/$', quiz_views.out_of_questions, name='out_of_questions'),
    url(r'^login/$', core_views.login_page, name='login'),
    url(r'^register/$', core_views.register, name='register'),
    url(r'^permission_denied/$', core_views.permission_denied, name='permission_denied'),
]
