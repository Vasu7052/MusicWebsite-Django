from django.http import HttpResponse

# Create your views here.

def index(request) :
    return HttpResponse("<h1>All albums will be listed here</h1>")


def detail(request , album_id) :
    return HttpResponse("<h1>Details for album id: " + str(album_id) + "</h1>")
