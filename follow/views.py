from django.shortcuts import render
from .models import UserModel, FollowModel

# Create your views here.
def view_test_follow(request):
    if request.method == 'GET':
        # 유저 전체 데이터 출력
        all_user = UserModel.objects.all()
        # print(f'all_user -> {all_user}')

        # 조건 - 팔로워 했는지 안했는지도 체크
        status_follow = FollowModel.objects.all()
        print(f'status_follow ->{status_follow}')
        # for status in status_follow:
        #     print(status.followee)
        return render(request, 'follow/test_follow.html', {'all_user': all_user, 'status_follow': status_follow})