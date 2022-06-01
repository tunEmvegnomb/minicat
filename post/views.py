from django.shortcuts import render, redirect
from .models import PostModel
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
        text = request.form['desc_give']
        print(text)
        file = request.files('file_give')

        print(text)
        return HttpResponse("업로드가 잘되었습니다")

