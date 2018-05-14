from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarsSerializer, OwnersSerializer
from .models import Car, Owner


class CarsView(APIView):

    http_method_names = ['get', 'head', 'post']

    def get(self, request, uuid=None):
        if uuid is not None:
            try:
                car = Car.objects.get(uuid=uuid)

            except Car.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            else:
                serializer = CarsSerializer(car, data=request.data, partial=True)
                if serializer.is_valid():
                    return Response(serializer.data)

        else:
            cars = Car.objects.all()
            serializer = CarsSerializer(cars, many=True)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OwnersView(APIView):

    http_method_names = ['get', 'head', 'post']

    def get(self, request):
        owners = Owner.objects.all()
        serializer = OwnersSerializer(owners, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OwnersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
