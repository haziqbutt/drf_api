from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Entry
from .serializers import EntrySerializer

@api_view(['GET'])
def all_entries(request):
    entries = Entry.objects.all()
    serializer = EntrySerializer(entries, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_entry(request):
    serializer = EntrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def one_entry(request, pk):
    try:
        entry = Entry.objects.get(pk=pk)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)
    except Entry.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_entry(request, pk):
    try:
        entry = Entry.objects.get(pk=pk)
        entry.delete()
        return Response({'message': 'Deleted successfully'})
    except Entry.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_entry(request, pk):
    try:
        entry = Entry.objects.get(pk=pk)
        data = request.data.copy()
        data['completed'] = True  
        serializer = EntrySerializer(entry, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Entry.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
