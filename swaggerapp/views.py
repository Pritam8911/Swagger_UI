from django.shortcuts import render
#from django.http import HttpResponse
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class InfoView(APIView):
    
    def get(self,request):
        infos=Info.objects.all()
        serializer=InfoSerializer(infos,many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(responses={200: InfoSerializer()},request_body=InfoSerializer)
    
    def post(self,request):
        serializer=InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
class AdvanceView(APIView):
    
    def get_info(self,pk):
        return Info.objects.get(pk=pk)

    def get(self,request,pk):
        info=self.get_info(pk)
        serializer=InfoSerializer(info)
        return Response(serializer.data)
    
    @swagger_auto_schema(responses={200: InfoSerializer()},request_body=InfoSerializer)
   
    def put(self,request,pk):
        info=self.get_info(pk)
        serializer=InfoSerializer(info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
    @swagger_auto_schema(responses={200: InfoSerializer()},request_body=InfoSerializer)
    
    def patch(self,request,pk):
        info=self.get_info(pk)
        serializer=InfoSerializer(info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
    def delete(self,request,pk):
        self.get_info(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
