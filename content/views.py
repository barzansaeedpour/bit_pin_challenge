from importlib.resources import contents
from django.shortcuts import render
from .models import Content
from .serializers import ContentSerializer
from score.models import Score
# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@permission_classes([AllowAny])
@api_view(['GET'])    
def get_contents(request):
    
    contents = Content.objects.all()

    ser = ContentSerializer(contents, many=True)

    for content in ser.data:
        scores = Score.objects.filter(content__pk = content["id"])
        if len(scores)==0:
            s = 0
        else:
            s = sum([i.score for i in scores]) / len(scores)
        content["score"] = s

    return Response(ser.data, status=status.HTTP_200_OK)

# def index(request):
#     all_contetns = Content.objects.all()
#     # ser = ContentSerializer(all_contetns, many = True)
#     context = {"contents":[]}
#     for c in all_contetns:
#         s = Score.objects.filter(content = c).first()
#         if s==None:
#             score = 0
#         else:
#             score = s.score

#         content={}
#         content["id"] = c.id
#         content["title"] = c.title
#         content["text"] = c.text
#         content["score"] = score

#         context["contents"].append(content)
#     print(context)
#     return render(request, 'index.html',context)
