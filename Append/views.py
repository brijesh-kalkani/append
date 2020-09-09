
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view



class SaveEmp(APIView):
    serializer_class = EmployeeSerializer
 
    def post(self, request):
        trade = request.data
        print(trade)
        serializer = EmployeeSerializer(data=trade)
        if serializer.is_valid(raise_exception=True):
            print(serializer.is_valid(raise_exception=True))
            serializer.save()
            return Response(trade,status=status.HTTP_200_OK)
        else:
            res = {'error': 'please provide full information'}
        return Response(res)