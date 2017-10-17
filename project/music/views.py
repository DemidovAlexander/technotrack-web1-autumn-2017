from django.shortcuts import render


def music(request, list_id=-1):
    return render(request, 'music.html', {'list_id': list_id})


def music_personality(request, post_id=-1):
    return render(request, 'music_personality.html', {'post_id': post_id})


def music_item(request, post_id=-1):
    return render(request, 'music_item.html', {'post_id': post_id})
