from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobpostingSerializer, JobpostingCreateSerializer, JobpostingUpdateSerializer, \
    JobPostingDetailSerializer, ApplymentSerializer
from .models import Jobposting, Apply
from django.db.models import Q


# Create your views here.
@api_view(['GET', 'POST'])
def PostList(request):
    if request.method == 'GET':
        jobpostings = Jobposting.objects.all()
        q = request.GET.get('q', '')
        if q:
            jobpostings = jobpostings.filter(
                Q(company__name__icontains=q) | Q(company__country__icontains=q) | Q(company__region__icontains=q) |
                Q(content__icontains=q) | Q(position__icontains=q) | Q(reward__icontains=q) | Q(skill__icontains=q))
        serializer = JobpostingSerializer(jobpostings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = JobpostingCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)


@api_view(['GET', 'PUT', 'DELETE'])
def PostDetail(request, pk):
    try:
        jobpostings = Jobposting.objects.get(id=pk)
    except jobpostings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobPostingDetailSerializer(jobpostings)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JobpostingUpdateSerializer(jobpostings, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        jobposting = Jobposting.objects.get(id=pk)
        jobposting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def ApplyPost(request, pk):
    try:
        apply = Apply.objects.all()
    except apply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        apply = apply.filter(jobposting_id_id=pk)
        serializer = ApplymentSerializer(apply, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ApplymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)
