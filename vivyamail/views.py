from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Mail
from .serializer import MailSerializer

class CreateMailView(CreateAPIView):
    serializer_class = MailSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class GetAllMailView(APIView):
    serializer_class=MailSerializer

    def get(self,request,*args,**kwargs):

        name_p=request.GET.get('name',None)

        if name_p:
            mails=Mail.objects.filter(name__icontains=name_p)
        else:
            mails=Mail.objects.all()
        serializer=MailSerializer(mails,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UpdateMailView(UpdateAPIView):
    serializer_class = MailSerializer
    lf='pk'

    def get_object(self):
        pk=self.kwargs.get(self.lf)
        return get_object_or_404(Mail,pk=pk)
    def put(self, request, *args, **kwargs):
        mails=self.get_object()
        serializer=self.get_serializer(mails,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteMailView(DestroyAPIView):
    serializer_class = MailSerializer
    lf='pk'

    def get_object(self):
        pk=self.kwargs.get(self.lf)
        return get_object_or_404(Mail,pk=pk)
    def delete(self, request, *args, **kwargs):
        mails=self.get_object()
        mails.delete()
        return Response({"message":f"id{mails.pk}deleted successfully"},status=status.HTTP_204_NO_CONTENT)
