from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from social_django.utils import load_backend, load_strategy
from social_core.exceptions import MissingBackend, AuthTokenError


def google_auth_redirect(request):
    return render(request, "index.html")

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def google_auth_callback(request):
    token = request.data["token"]

    try:
        backend = load_backend(load_strategy(request), "google-oauth2", redirect_url=None)
        user = backend.do_auth(token)

        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Invalid token"}, status=400)

    except (MissingBackend, AuthTokenError) as e:
        return Response({"error": str(e)}, status=400)

