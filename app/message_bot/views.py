import json

from config.settings import DEBUG

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .bot import webhook_handler


@api_view(['POST'])
def webhook(request):
    if DEBUG:
        print(json.dumps(request.data, indent=2, ensure_ascii=False))

    webhook_handler(request.data)
    return Response('ok')
