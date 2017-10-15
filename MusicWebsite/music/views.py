from django.http import HttpResponse
from django.http import Http404
from .models import Album
from django.template import loader
from django.shortcuts import render , get_object_or_404

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

            # OR

'''
def index(request) :
    all_albums = Album.objects.all()
    template = loader.get_template("music/index.html")
    # Create a dictionary ..
    context = {"all_albums" : all_albums}
    return HttpResponse(template.render(context,request))
'''

            # OR

def index(request) :
    all_albums = Album.objects.all()
    # Create a dictionary ..
    context = {"all_albums" : all_albums}
    return render(request , "music/index.html" , context)

'''

def detail(request , album_id) :
    try :
        album = Album.objects.get(pk=album_id)
        album_title = album.album_title
        album_logo = album.album_logo
        all_songs = album.song_set.all()
        context = {"all_songs": all_songs , "album_title" : album_title , "album_logo" : album_logo}
    except Album.DoesNotExist :
        raise Http404("Album does not exist")
    return render(request , "music/detail.html" , context)
'''

                    # OR

def detail(request , album_id) :
    album = get_object_or_404(Album , pk=album_id)
    album_title = album.album_title
    album_logo = album.album_logo
    all_songs = album.song_set.all()
    context = {"all_songs": all_songs , "album_title" : album_title , "album_logo" : album_logo}
    return render(request , "music/detail.html" , context)