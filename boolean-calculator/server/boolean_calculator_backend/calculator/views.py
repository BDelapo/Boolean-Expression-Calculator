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
        request.session['term'] = calculations.calculate(request.data['term'])
        # print(request.data['term'])
        resp = Response()
        return resp

    def get(self, request):
        print(request.session['term'])
        return Response(request.session['term'])

