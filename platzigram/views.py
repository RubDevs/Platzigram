from django.http import HttpResponse

from datetime import datetime
import json


def hello(request):
    return HttpResponse('Hello! Current time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sorted(request):
    ints = [int(x) for x in request.GET["numbers"].split(",")]
    sortedInts = sorted(ints)
    data = {
        "status": "ok",
        "numbers": sortedInts,
        "message": "numbers sorted successfully"
    }
    return HttpResponse(json.dumps(data))


def hi(request, name, age):
    if age < 12:
        message = "Sorry {} you are not allowed here".format(name)
    else:
        message = "Hi {} welcome to Platzigram".format(name)
    return HttpResponse(message)
