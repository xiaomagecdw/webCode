#conding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'xiaomagecdw' and password == '123456':
            #return HttpResponseRedirect('/event_manage/')
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user', username, 3600)
            request.session['user'] = username
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password Error! Plase try again!'})
    else:
        return render(request, 'index.html', {'error': 'username or password Error! Plase try again!'})



def event_manage(request):
    #return render(request, "event_manage.html")
    #username = request.COOKIES.get('user', '')
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user":username})
