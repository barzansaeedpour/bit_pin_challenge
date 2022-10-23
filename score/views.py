from django.shortcuts import render
from content.models import Content
from django.shortcuts import redirect
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from score.models import Score


# Create your views here.
@permission_classes([AllowAny])
@api_view(['POST'])    
def submit_score(request):
    user = request.user
    data = request.data

    content = Content.objects.filter(pk=data["content_id"]).first()

    s = Score.objects.filter(user = user , content=content).first()
    
    if s==None:
        score = Score.objects.create(content= content,score=data["score"],user = user)
        score.save()
        return Response({"message":"امتیاز با موفقیت ثبت شد"}, status=status.HTTP_200_OK)
    else:
        # update the score
        s.score = data["score"]
        s.save()
        return Response({"message":"امتیاز با موفقیت بروز رسانی شد"}, status=status.HTTP_200_OK)




# def detail(request):
    
#     # all_contetns = Content.objects.filter(pk==)
#     # # ser = ContentSerializer(all_contetns, many = True)
#     # context = {"contents":[]}
#     # for c in all_contetns:
#     #     s = Score.objects.filter(content = c).first()
#     #     if s==None:
#     #         score = 0
#     #     else:
#     #         score = s.score

#     #     content={}
#     #     content["id"] = c.id
#     #     content["title"] = c.title
#     #     content["text"] = c.text
#     #     content["score"] = score

#     #     context["contents"].append(content)
#     # print(context)
#     return render(request, 'detail.html')


# def update_score(request):
#     body = request.body
#     # all_contetns = Content.objects.filter()
#     # # ser = ContentSerializer(all_contetns, many = True)
#     # context = {"contents":[]}
#     # for c in all_contetns:
#     #     s = Score.objects.filter(content = c).first()
#     #     if s==None:
#     #         score = 0
#     #     else:
#     #         score = s.score

#     #     content={}
#     #     content["id"] = c.id
#     #     content["title"] = c.title
#     #     content["text"] = c.text
#     #     content["score"] = score

#     #     context["contents"].append(content)
#     # print(context)
#     return redirect('/')
