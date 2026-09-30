import os
from django.conf import settings
from django.http import JsonResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application

settings.configure(
    DEBUG=False,
    ALLOWED_HOSTS=["*"],
    ROOT_URLCONF=__name__,
    SECRET_KEY="mini-django-test-key",
)

def index(request):
    return JsonResponse({"message": "mini-django en ligne", "env_test": os.environ.get("TEST_VAR", "(non définie)")})

urlpatterns = [path("", index)]
application = get_wsgi_application()
