from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from tag.models.tag_model import Tag
from tag.serializers.tag_serializer import TagSerializer


class TagRestView(APIView):
    serializer_class = TagSerializer

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(instance=Tag.objects.get(pk=pk), validated_data=serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        if tag:
            tag.delete()
            return Response("Success!", status=status.HTTP_202_ACCEPTED)
        return Response("Failure!", status=status.HTTP_400_BAD_REQUEST)
