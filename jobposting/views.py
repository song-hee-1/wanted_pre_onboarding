from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobpostingSerializer
from .models import Jobposting


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/jobposting-list/',
        'Detail View': '/jobposting-detail/<str:pk>/',
        'Create': '/jobposting-create/',
        'Update': '/jobposting-update/<str:pk>/',
        'Delete': '/jobposting-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def jobpostingList(request):
    jobpostings = Jobposting.objects.all()
    serializer = JobpostingSerializer(jobpostings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def jobpostingDetail(request, pk):
    jobpostings = Jobposting.objects.get(id=pk)
    serializer = JobpostingSerializer(jobpostings, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def jobpostingCreate(request):
    serializer = JobpostingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def jobpostingUpdate(request, pk):
    jobposting = Jobposting.objects.get(id=pk)
    serializer = JobpostingSerializer(instance=jobposting, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def jobpostingDelete(request, pk):
    jobposting = Jobposting.objects.get(id=pk)
    jobposting.delete()

    return Response('Item succsesfully delete!')

