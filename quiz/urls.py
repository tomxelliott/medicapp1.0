from django.conf.urls import url, include
# from django.contrib.auth import views as auth_views

from views import quiz_views
from views import core_views

app_name = 'quiz'
urlpatterns = [
    url(r'^$', quiz_views.index, name='index'),
    url(r'^(?P<topic_id>[0-9]+)/question/$', quiz_views.question, name='question'),
    url(r'^(?P<question_id>[0-9]+)/$', quiz_views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/answer/$', quiz_views.answer, name='answer'),
    url(r'^out_of_questions/$', quiz_views.out_of_questions, name='out_of_questions'),
    url(r'^about_us/$', quiz_views.about_medicapp, name='about_us'),
    url(r'^faq/$', quiz_views.faq, name='faq'),
    url(r'^login/$', core_views.user_login, name='login'),
    url(r'^logout/$', core_views.user_logout, name='logout'),
    url(r'^register/$', core_views.register, name='register'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', core_views.user_profile, name='profile'),
    url(r'^permission_denied/$', core_views.permission_denied, name='permission_denied'),

    # url('^', include('django.contrib.auth.urls')),
]
