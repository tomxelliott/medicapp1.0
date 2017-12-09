from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from django.template.context_processors import csrf
from django.views.decorators.cache import never_cache

from forms import UserForm, UserProfileForm
from django.shortcuts import render_to_response

from .models import Topic, Question, Choice, User
from .models import UserProfile


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("quiz/index.html")
            else:
                return HttpResponse("You're account is disabled.")
        else:
            print  "invalid login details " + username + " " + password
            return render_to_response('quiz/login.html', {}, context)
    else:
        # the login is a GET request, so just show the user the login form.
        return render_to_response('quiz/login.html', {}, context)


@login_required
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('quiz/index.html')


def register(request):
    context = RequestContext(request)
    print context
    registered = False
    if request.method == 'POST':
        u_f = UserForm(data=request.POST)
        p_f = UserProfileForm(data=request.POST)
        if u_f.is_valid() and p_f.is_valid():
            user = u_f.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            profile = p_f.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print u_f.errors, p_f.errors
    else:
        u_f = UserForm()
        p_f = UserProfileForm()

    return render_to_response('quiz/register.html', {'u_f': u_f, 'p_f': p_f, 'registered': registered},
                              context)


def permission_denied(request):
    user = request.user
    template = loader.get_template('quiz/permission_denied.html')

    context = {}
    context.update(csrf(request))
    return HttpResponseForbidden(template.render(context))