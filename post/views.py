from django.shortcuts import render, redirect
from .models import PostModel
import requests
# from rest_framwork.views import API
# from datetime import datetime, timedelta

from django.http import HttpResponse

# Create your views here.
def home(request):
    return redirect('/post')

def post(request):
    if request.method == 'GET':
        all_post = PostModel.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'post': all_post})
    elif request.method == 'POST':
        # author = request.user
        # text = request.POST.get('desc_give','')
        file = request.data.get('file')
        return HttpResponse("업로드가 잘되었습니다")

def get_catfact(request):
    request_catfact = requests.get('https://meowfacts.herokuapp.com/')
    content_catfact = request_catfact.text.strip('{"data":}[""]')
    print(f'content->{content_catfact}')
    return content_catfact
