from rest_framework.response import Response
from rest_framework.views import APIView
from . import calculations


class Session_Auth(APIView):

    def post(self, request):
        r = request.session.session_key
        request.session.save()
        resp = Response()
        return resp


class Row_Obtainer(APIView):

    def post(self, request):
        # print(request.session['term'])
        # request.session['term'] = calculations.calculate(request.data.term)
        # print(request.session['term'])
        resp = Response()
        return resp

    def get(self, request):
        # print(request.session['term'])
        return Response(request.session['term'])

    # def post(self, request):

    #     request.session.save()
    #     return Response(request.session.session_key)

    # def get(self, request):
    #     print(request.GET['sess_id'])
    #     return Response(request.data)


# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def example_view(request, format=None):
#     content = {
#         'user': str(request.user),  # `django.contrib.auth.User` instance.
#         'auth': str(request.auth),  # None
#     }
#     return Response(content)


# @api_view(['POST'])
# def setSession(request):
#     routes = [
#         'POST /set-session'
#     ]
#     request.session.save()
#     terms = {}
#     if request.method == 'POST':
#         print(request.session._session_key)
#         request.session['id'] = request.session._session_key
#         terms = request.data
#         request.session['id'] = 55
#         return Response(request.session._session_key)

#     elif request.method == 'GET':
#         print(request.data)
#         return Response(request.data)
    

# @api_view(['POST'])
# def getRows(request):
#     print(request.session.keys())    

#     routes = [
#         'POST /calculate-terms'
#     ]
#     print(request.session.get('id'))
#     return Response(request.session.get('id'))