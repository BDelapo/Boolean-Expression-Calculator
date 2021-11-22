from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def setSession(request):
    routes = [
        'POST /'
        'POST /calculate-terms'
    ]
    print()
    request.session['id'] = request.data
    return Response(request.session['id'])

@api_view(['POST'])
def getRows(request):
    # print(request.session['id'])
    return Response()