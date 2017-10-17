from django.shortcuts import render


def movies(request, list_id=-1):
    return render(request, 'movies.html', {'list_id': list_id})


def movies_personality(request, post_id=-1):
    return render(request, 'movies_personality.html', {'post_id': post_id})


def movies_item(request, post_id=-1):
    return render(request, 'movies_item.html', {'post_id': post_id})
