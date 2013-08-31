from django.shortcuts import render_to_response

def index(request):
    return render_to_response('user_index.html')

def login(request):
    return render_to_response('user_login')

def logout(request):
    return render_to_response('user_logout')

def register(request):
    return render_to_response('user_register')
