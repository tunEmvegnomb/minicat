from django.shortcuts import render
from .models import UserModel, FollowModel

# Create your views here.
def view_test_follow(request):
    if request.method == 'GET':
        all_user = UserModel.objects.all()
        print(f'all_user -> {all_user}')
        return render(request, 'follow/test_follow.html', {'all_user': all_user})