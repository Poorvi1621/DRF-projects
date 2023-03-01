
from rest_framework.views import APIView
from rest_framework.response import Response

class AnimalView(APIView):

    def get(self, request):

        return Response(
            {
             'status' : True,
             'messgae':"animal fetched using GET"

            })



    def post(self, request):
        return Response(
            {
            'status' : True,
             'messgae':"animal fetched using POST"

            })


    def put(self, request):
        return Response(
            {
            'status' : True,
             'messgae':"animal fetched using PUT"

            })

    def patch(self, request):
        return Response(
            {
            'status' : True,
             'messgae':"animal fetched using PATCH"

            })
    
    def delete(self, request):
        
        return Response(
            {
            'status' : True,
             'messgae':"animal fetched using DELETE"

            })
