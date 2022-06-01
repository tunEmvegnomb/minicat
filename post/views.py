from django.shortcuts import render, redirect
from .models import PostModel
from .forms import UploadFileForm
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
        file = UploadFileForm(request.POST, request.FILES)
        print(file)

        return HttpResponse("업로드가 잘되었습니다")

