from django.shortcuts import render


def paintings(request, list_id=-1):
    return render(request, 'paintings.html', {'list_id': list_id})


def paintings_personality(request, post_id=-1):
    return render(request, 'paintings_personality.html', {'post_id': post_id})


def paintings_item(request, post_id=-1):
    return render(request, 'paintings_item.html', {'post_id': post_id})
