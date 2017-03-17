

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from medals.models import FullyUser, FullyBikeTracker
from medals.serializers import FullyUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import loader 
from django.shortcuts import render

@api_view(['GET', 'POST'])
def FullyUser_list(request):
    """
    list users or create new
    """
    if request.method == 'GET':
        fullyUsers = FullyUser.objects.all()
        serializer = FullyUserSerializer(fullyUsers, many=True)
        print('Method GET')
        return Response(serializer.data)


    elif request.method =='POST':
        serializer = FullyUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def FullyUser_detail(request, pk):
    """
    get individual details
    """
    try:
        fullyUser = FullyUser.objects.get(pk=pk)
    except FullyUser.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = FullyUserSerializer(fullyUser)
        
        return Response(serializer.data)
    
    elif  request.method == 'PUT':
        serializer = FullyUserSerializer(fullyUser, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        fullyUser.delete()
        return Response(status=204)


def index(request):
    all_users = FullyUser.objects.all()
    context = {
        'all_users': all_users,
    }
    return render(request, 'medals/index.html', context)