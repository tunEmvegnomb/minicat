from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/') 
        else:
            return render(request, 'user/signup.html') 
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            return render(request, 'user/signup.html', {'error':'username 또는 password를 확인해주세요'})  #
        exist_user = get_user_model().objects.filter(username=username)
        if exist_user:
            return render(request, 'user/signup.html', {'error':'해당 username은 사용 중입니다'}) #
        else:
            UserModel.objects.create_user(username=username, password=password)
        return redirect('/sign-in')
    
    
def sign_in(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error':'username 또는 password를 확인해주세요'})

        
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')




