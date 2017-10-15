from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def user(request, user=None):
    return render(request, 'user.html', {'user': user})


def personalities(request, list_id=None):
    return render(request, 'personalities.html', {'list_id': list_id})


def personality(request, post_id=-1):
    return render(request, 'personality.html', {'post_id': post_id})


def music(request, list_id=-1):
    return render(request, 'music.html', {'list_id': list_id})


def music_personality(request, post_id=-1):
    return render(request, 'music_personality.html', {'post_id': post_id})


def music_item(request, post_id=-1):
    return render(request, 'music_item.html', {'post_id': post_id})


def movies(request, list_id=-1):
    return render(request, 'movies.html', {'list_id': list_id})


def movies_personality(request, post_id=-1):
    return render(request, 'movies_personality.html', {'post_id': post_id})


def movies_item(request, post_id=-1):
    return render(request, 'movies_item.html', {'post_id': post_id})


def books(request, list_id=-1):
    return render(request, 'books.html', {'list_id': list_id})


def books_personality(request, post_id=-1):
    return render(request, 'books_personality.html', {'post_id': post_id})


def books_item(request, post_id=-1):
    return render(request, 'books_item.html', {'post_id': post_id})


def paintings(request, list_id=-1):
    return render(request, 'paintings.html', {'list_id': list_id})


def paintings_personality(request, post_id=-1):
    return render(request, 'paintings_personality.html', {'post_id': post_id})


def paintings_item(request, post_id=-1):
    return render(request, 'paintings_item.html', {'post_id': post_id})


def references(request, list_id=-1):
    return render(request, 'references.html', {'list_id': list_id})


def reference(request, post_id=-1):
    return render(request, 'reference.html', {'post_id': post_id})
