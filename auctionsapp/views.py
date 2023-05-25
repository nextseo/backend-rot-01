from django.shortcuts import render , HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .models import auction_topic , test
from .serializers import Auction_Topic_Serializer ,Test2_Serializer
# Create your views here.
from datetime import datetime

def hellow(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def AucListView(request):
    try:
        if request.method == 'GET':
            snippets = auction_topic.objects.all()
            serializer = Auction_Topic_Serializer(snippets,  many=True)
            return Response(serializer.data)
        elif request.method == 'POST':

            serializer = Auction_Topic_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as data:
        data = {'message': 'เกิดข้อผิดพลาด'}
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['PUT'])
@authentication_classes([])
@permission_classes([])
def aucedit(request, pk):
    try:
        Customer = auction_topic.objects.get(pk=pk)
    except auction_topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = Auction_Topic_Serializer(Customer, data=request.data)
    if serializer.is_valid():
        serializer.save()

        # return Response({'status': 'ok', 'message': 'User created successfully'}, status=201)

        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def aucdel(request, pk):
    try:
        product = auction_topic.objects.get(pk=pk)
    except auction_topic.DoesNotExist:
        data = {'message': 'เกิดข้อผิดพลาด'}

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    data = {'message': 'ลบข้อมูลแล้ว'}

    return Response(data, status=status.HTTP_204_NO_CONTENT)





@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def TESTView(request):
    try:
        if request.method == 'GET':
            snippets = test.objects.all()
            serializer = Test2_Serializer(snippets,  many=True)
            return Response(serializer.data)
        elif request.method == 'POST':

            serializer = Test2_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as data:
        data = {'message': 'เกิดข้อผิดพลาด'}
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
