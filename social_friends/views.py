from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from rest_framework.views import APIView
from .models import SocialMediaUser
# Create your views here.

class UsersView(APIView):
    def get(self, request):
        users = SocialMediaUser.objects.all()
        return JsonResponse({"data": [{'id': x.id, 'first_name': x.first_name, 'last_name': x.last_name} for x in users], "status_code": 200, "message": "success"}, safe=False)

class UserFriendView(APIView):
    def get(self, request, friends):
        frnd_lst = []
        user_id = request.query_params.get('user_id')
        try:
            if user_id and friends:
                friends = SocialMediaUser.objects.get(id=user_id).friends.all()
                frnd_lst = [{'id': x.id, 'first_name': x.first_name, 'last_name': x.last_name} for x in friends]
            
            elif user_id and not friends:
                friends = SocialMediaUser.objects.get(id=user_id).friends.values('id')
                non_friends = SocialMediaUser.objects.exclude(id__in = friends)
                frnd_lst = [{'id': x.id, 'first_name': x.first_name, 'last_name': x.last_name} for x in non_friends]

        except ObjectDoesNotExist as err:
            return JsonResponse({"data": frnd_lst, "status_code": 400, "message": str(err)}, safe=False)

        except MultipleObjectsReturned as err:
            return JsonResponse({"data": frnd_lst, "status_code": 400, "message": str(err)}, safe=False)
        
        except Exception as err:
            return JsonResponse({"data": frnd_lst, "status_code": 400, "message": str(err)}, safe=False)

        return JsonResponse({"data": frnd_lst, "status_code": 200, "message": "success"}, safe=False)

class CommonFriendView(APIView):
    def get(self, request):
        frnds = []
        user_1 = request.query_params.get('user1')
        user_2 = request.query_params.get('user2')
        try:
            social_users = SocialMediaUser.objects.filter(id__in = [user_1, user_2])
            friend_sets = [x.friends.all() for x in social_users]
            common_frnds = friend_sets[0].intersection(friend_sets[1])
            frnds = [{"id": x.id, "first_name": x.first_name, "last_name": x.last_name} for x in common_frnds]
        except Exception as err:
            return JsonResponse({"data": frnds, "status_code": 400, "message": str(err)}, safe=False)
 
        return JsonResponse({"data": frnds, "status_code": 200, "message": "success"}, safe=False)

class PotentialFriendView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        potential_friends = set()
        frnds = []
        
        def check_friends_depth(frnd):
            if frnd.friends.filter(id=user_id).count() == 0:
                potential_friends.add(frnd)
                return True
            else:
                return False
            
        try:
            if user_id:
                frnds = SocialMediaUser.objects.get(id=user_id).friends.all()
                [tuple(filter(check_friends_depth, _fof.friends.exclude(id=user_id))) for _fof in frnds]
                frnds = [{"id": x.id, "first_name": x.first_name, "last_name": x.last_name} for x in potential_friends]
        except Exception as err:
            return JsonResponse({"data": [], "status_code": 400, "message": str(err)}, safe=False)
 
        return JsonResponse({"data": frnds, "status_code": 200, "message": "success"}, safe=False)

class AddFriendView(APIView):
    def post(self, request):
        message = "Added successfully"
        user_id = request.data.get("user_id", None)
        friends = request.data.get("friends")
        try:
            if user_id:
                user = SocialMediaUser.objects.get(id=user_id)
                for frnd in friends:
                    user.friends.add(SocialMediaUser.objects.create(first_name = str(frnd['first_name']), last_name = str(frnd['last_name'])))
            else:
                message = "Missing query parameters"

        except Exception as err:
            return JsonResponse({"status_code": 200, "message": str(err)}, safe=False)

        return JsonResponse({"status_code": 200, "message": message}, safe=False)
           