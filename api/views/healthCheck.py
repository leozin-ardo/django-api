from telnetlib import STATUS
from django.http import HttpResponse

def handler (request):
    return HttpResponse(status=200, content="OK")