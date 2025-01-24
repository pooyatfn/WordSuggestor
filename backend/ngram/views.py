from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import NGramManager

ngram_manager = NGramManager()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_ngram_api(request):
    data = request.data
    text = data.get('text')
    dataset_name = data.get('dataset_name', 'fa')
    result = ngram_manager.add_ngram(text, dataset_name)
    return Response({'result': result})


@api_view(['GET'])
def suggest_word_api(request):
    text = request.GET.get('text', '')
    dataset_name = request.GET.get('dataset', 'fa')
    suggestion = ngram_manager.suggest_word(text, dataset_name)
    return Response({'suggestions': suggestion})
