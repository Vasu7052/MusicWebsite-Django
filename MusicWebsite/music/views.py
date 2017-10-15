from django.http import HttpResponse
from .models import Album
from django.template import loader

# Create your views here.

'''
def index(request) :
    all_albums = Album.objects.all()
    html = ""
    for f in all_albums :
        url = "/music/" + str(f.id) + "/"
        html += '<a href="'+url+'" > ' + f.album_title + "</a><br>"

    return HttpResponse(html)
'''

def index(request) :
    all_albums = Album.objects.all()
    template = loader.get_template("music/index.html")
    # Create a dictionary ..
    context = {
        "all_albums" : all_albums
    }
    return HttpResponse(template.render(context,request))

def detail(request , album_id) :
    return HttpResponse("<h1>Details for album id: " + str(album_id) + "</h1>")
