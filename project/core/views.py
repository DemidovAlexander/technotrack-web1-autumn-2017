from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def user(request, user=None):
    return render(request, 'user.html', {'user': user})


def personalities(request, user=None):
    return render(request, 'personalities.html', {'user': user})


def personality(request, user=None, post_id=-1):
    return render(request, 'personality.html', {'user': user, 'post_id': post_id})


def music(request, user=None):
    return render(request, 'music.html', {'user': user})


def music_personality(request, user=None, post_id=-1):
    return render(request, 'music_personality.html', {'user': user, 'post_id': post_id})


def music_item(request, user=None, post_id=-1):
    return render(request, 'music_item.html', {'user': user, 'post_id': post_id})


def movies(request, user=None):
    return render(request, 'movies.html', {'user': user})


def movies_personality(request, user=None, post_id=-1):
    return render(request, 'movies_personality.html', {'user': user, 'post_id': post_id})


def movies_item(request, user=None, post_id=-1):
    return render(request, 'movies_item.html', {'user': user, 'post_id': post_id})


def books(request, user=None):
    return render(request, 'books.html', {'user': user})


def books_personality(request, user=None, post_id=-1):
    return render(request, 'books_personality.html', {'user': user, 'post_id': post_id})


def books_item(request, user=None, post_id=-1):
    return render(request, 'books_item.html', {'user': user, 'post_id': post_id})


def paintings(request, user=None):
    return render(request, 'paintings.html', {'user': user})


def paintings_personality(request, user=None, post_id=-1):
    return render(request, 'paintings_personality.html', {'user': user, 'post_id': post_id})


def paintings_item(request, user=None, post_id=-1):
    return render(request, 'paintings_item.html', {'user': user, 'post_id': post_id})


def references(request, user=None):
    return render(request, 'references.html', {'user': user})


def reference(request, user=None, post_id=-1):
    return render(request, 'reference.html', {'user': user, 'post_id': post_id})
