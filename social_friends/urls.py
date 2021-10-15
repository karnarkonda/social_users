
from django.urls import path, include
from .views import UsersView, UserFriendView, CommonFriendView

urlpatterns = [
    path("users", UsersView.as_view()),
    path("user/friends", UserFriendView.as_view(), {"friends": True}),
    path("user/not_friends", UserFriendView.as_view(), {"friends": False}),
    path("user/common_friends", CommonFriendView.as_view()), 
]