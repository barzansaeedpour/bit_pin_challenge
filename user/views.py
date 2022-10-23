from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import requests
import json
from .serializers import UserSerializer,AccessLevelSerializer,UserAccessLevelSerializer
from .models import Role,AccessLevel,UserAccessLevel,Profile
from core import settings
from django.contrib.auth import authenticate
import random

# import pandas as pd
@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    ser = UserSerializer(data = request.data)
  
    #ser.data["token"]=token
    if ser.is_valid():
        ser.save()
        u = update_profile(request)
        print(ser.data)
        r = requests.post(settings.url+'/api-token-auth',data={"username":ser.data["username"],"password":ser.data['password']}, params=request.POST)
        # token = Token.objects.get(pk=ser.data["id"])
        # print(token)
        y = json.loads(r.text)
        # ser.data['token']=y["token"] 
        h = ser.data
        h.update(u)
        # print(type(h))
        h["token"] = y["token"]

        return Response(h ,status = status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @permission_classes((IsAuthenticated, IsOwner))
# def profile(request):
#     try:
#         user = User.objects.get(username=request.query_params['username'])
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     ser = UserSerializer(user)
#     return Response(ser.data, status=status.HTTP_200_OK)

def update_profile(request):
    user = User.objects.get(username=request.data["username"])
    user.profile.phone_number = request.data["phone_number"]
    user.profile.birth_date = request.data["birth_date"]
    user.profile.jensiat = request.data["jensiat"]
    role = Role.objects.filter(pk=request.data["role"]).first()
    user.profile.role = role
    user.save()
    # print(user)
    return request.data
    # return Response(request.data ,status = status.HTTP_200_OK)


# 72af81f1f34054fa51c945a837f1bc6956eb75e7


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     user = authenticate(username=request.data["username"], password=request.data["password"])
#     if user is not None:
#         u = User.objects.filter(username=request.data["username"]).first()
#         h={}
#         token = Token.objects.filter(user=u)
#         h["token"]=str(token.first())
#         h["username"]=u.username
#         return Response(h ,status = status.HTTP_200_OK)
#     else:
#         h={}
#         h["message"]="اطلاعات ورودی اشتباه است"
#         return Response(h, status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    u = authenticate(username=request.data["username"], password=request.data["password"])
    # user = User.objects.filter(username=request.data["username"])
    # ser = UserSerializer(data = request.data)
    if u is not None:
        user = User.objects.filter(username=request.data["username"])
        h={}
        token = Token.objects.filter(user=user[0])
        access_levels = UserAccessLevel.objects.filter(user=user[0])
        ser = UserAccessLevelSerializer(access_levels,many= True)
        p = Profile.objects.filter(user=user[0])[0]
        
        h["token"]=str(token.first())
        h["username"]=user[0].username
        h["first_name"]=user[0].first_name
        h["last_name"]=user[0].last_name
        h["phone_number"]=p.phone_number
        h["birth_date"]=p.birth_date
        h["company_id"]=p.company.pk
        h["company_name"]=p.company.title
        h["access_levels"]=ser.data
        
        return Response(h ,status = status.HTTP_200_OK)
    else:
        h={}
        h["message"]="اطلاعات ورودی اشتباه است"
        return Response(h, status = status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def forget_password(request):
    # token = request.auth
    # token = Token.objects.filter(key=token)
    # user_id = token.values()[0]['user_id']
    # user = User.objects.filter(id=user_id).first()
    
    p = Profile.objects.filter(phone_number=request.data['phone_number']).first()
    user = p.user
    phone_number=user.profile.phone_number
    user_list = []
    
    user_list.append(phone_number)
    new_password = str(random.randint(100000, 999999))
    txt = 'رمز جدید شما: ' + new_password
    url = "http://87.107.121.52/post/sendsms.ashx?from=50002237171&to="+str(user_list)+"&text="+str(txt)+"&password=nim@123@nim&username=westco"        
    r = requests.post(url)
    user = User.objects.filter(username=user).first()
    if r.status_code == 200:
        user.set_password(new_password)
        user.save()
        
    
    print("*********************************")
    print("*********************************")
    print("*********************************")
    print("new_password: ",new_password)
    return Response({"message":"رمز با موفقیت بازنشانی شد"}, status = status.HTTP_200_OK)


@api_view(['POST'])
def change_password(request):
    data = request.data
    token = request.auth
    token = Token.objects.filter(key=token)
    user_id = token.values()[0]['user_id']
    user = User.objects.filter(id=user_id).first()
    if data["password1"]==data["password2"]:
        user.set_password(data["password1"])
        user.save()
        return Response({"message":"تغییر رمز با موفقیت انجام شد."}, status = status.HTTP_200_OK)
    else:    
        return Response({"message":""}, status = status.HTTP_200_OK)
    
@api_view(['GET'])
# @permission_classes([AllowAny])
def access_levels(request):
    token = request.auth
    user_token = Token.objects.filter(key=token)
    user_id = user_token.values()[0]['user_id']
    user = User.objects.filter(pk = user_id)
    
    if len(user)>0:
        h={}
        access_levels = UserAccessLevel.objects.filter(user=user[0])
        ser = UserAccessLevelSerializer(access_levels,many= True)        
        h["username"]=user[0].username
        h["access_levels"]=ser.data
        return Response(h ,status = status.HTTP_200_OK)
    else:
        h={}
        h["message"]="کاربر وجود ندارد"
        return Response(h, status = status.HTTP_404_NOT_FOUND)












