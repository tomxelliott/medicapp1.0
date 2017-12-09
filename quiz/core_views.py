from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.views.decorators.cache import never_cache

from models import UserProfile
from forms import UserForm, UserProfileForm
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .forms import LoginForm

from .models import Topic, Question, Choice, User


@never_cache
def login_vw(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("home")

    err_msg = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            password = form.cleaned_data['password']
            user = authenticate(username=userid, password=password)
            template = loader.get_template('hr/login.html')
    else:
        form = LoginForm()
    # return user to login page
    return render_to_response('hr/login.html', \
                              {'form': form, 'err_msg': err_msg, }, \
                              context_instance=RequestContext(request))


@login_required(login_url='../login')
def permission_denied(request):
    user = request.user
    template = loader.get_template('hr/permission_denied.html')

    context = {}
    context.update(csrf(request))
    return HttpResponseForbidden(template.render(context))