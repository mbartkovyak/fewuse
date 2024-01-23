from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def accept_telegram_message(request):
    print(request.date)

    return Response({'status': 'Success'})
