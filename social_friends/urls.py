
from django.urls import path, include
from .views import UsersView, UserFriendView, CommonFriendView, PotentialFriendView, AddFriendView

urlpatterns = [
    path("users", UsersView.as_view()),
    path("user/friends", UserFriendView.as_view(), {"friends": True}),
    path("user/not_friends", UserFriendView.as_view(), {"friends": False}),
    path("user/common_friends", CommonFriendView.as_view()), 
    path("user/potential_friends", PotentialFriendView.as_view()),
    path("user/add_friends", AddFriendView.as_view()), 
]