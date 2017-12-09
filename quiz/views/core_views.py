from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie

from quiz.models import UserProfile
from quiz.forms import UserForm, UserProfileForm
from django.shortcuts import render_to_response


@ensure_csrf_cookie
def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/quiz/")
            else:
                return HttpResponse("You're account is disabled.")
        else:
            print "invalid login details " + username + " " + password
            return render_to_response('quiz/login.html', {}, context)
    else:
        return render_to_response('quiz/login.html', {}, context)


@ensure_csrf_cookie
def user_profile(request, user_id):
    context = RequestContext(request)
    return render_to_response('quiz/profile.html', {}, context)


@login_required
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('/quiz/')


@ensure_csrf_cookie
def register(request):
    context = RequestContext(request)
    print context
    registered = False
    if request.method == 'POST':
        u_f = UserForm(data=request.POST)
        if u_f.is_valid():
            user = u_f.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            registered = True
        else:
            print u_f.errors
    else:
        u_f = UserForm()

    return render_to_response('quiz/register.html', {'u_f': u_f, 'registered': registered},
                              context)


def permission_denied(request):
    user = request.user
    template = loader.get_template('quiz/permission_denied.html')
    context = {}
    context.update(csrf(request))
    return HttpResponseForbidden(template.render(context))


def csrf_failure(request, reason=""):
    context = {'message': 'You shouldn\'t be here!'}
    return render_to_response('/403.html', context)