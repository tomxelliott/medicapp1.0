from django.conf.urls import url

from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<topic_id>[0-9]+)/question/$', views.question, name='question'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
    url(r'^out_of_questions/$', views.out_of_questions, name='out_of_questions'),
]
