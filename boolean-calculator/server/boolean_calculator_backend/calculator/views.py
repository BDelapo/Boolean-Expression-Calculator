from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from . import calculations
import asyncio


@api_view(['POST'])
def post_session(request):
    if 'term' in request.session.keys():
        del request.session['term']
    request.session.session_key
    request.session.save()
    resp = Response()
    return resp

@api_view(['POST'])
def post(request):
    # await Row_Obtainer.lock.acquire()
    request.session['term'] = calculations.calculate(request.data['term'])
    resp = Response(request.data)
    return resp

@api_view(['GET'])
def get(request):
    # await Row_Obtainer.lock.acquire()
    print(1)
    return Response(request.session['term'])


