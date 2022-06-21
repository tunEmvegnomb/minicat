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
        try:
            latest_catfact = request.session['catfact']
        except:
            latest_catfact = '아직 조회하지 않았다옹'
        return render(request, 'home.html', {'post': all_post, 'catfact':latest_catfact})
    elif request.method == 'POST':

        img_file = request.FILES.get('file_upload', '')
        text = request.POST.get('text123', '')
        print("1번")
        print(text)
        print(img_file)
        print("2번")
        my_post = PostModel.objects.create(filename=img_file, text=text)
        my_post.save()

        return HttpResponse("업로드가 잘되었습니다")
        # return redirect('/')

def get_catfact(request):
    request_catfact = requests.get('https://meowfacts.herokuapp.com/')
    content_catfact = request_catfact.text.strip('{"data":}[""]')
    request.session['catfact'] = content_catfact
    return redirect('/')
