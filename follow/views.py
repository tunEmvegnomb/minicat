from django.shortcuts import render

# Create your views here.
def view_test_follow(request):
    return render(request, 'follow/test_follow.html')