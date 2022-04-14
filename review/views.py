from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer
from . models import Review

# Create your views here.

@api_view(['GET'])
def review_table(request, fk):
    review = get_list_or_404(Review)
    
    if request.method == 'GET':
        review = Review.objects.filter(product_id=fk)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
