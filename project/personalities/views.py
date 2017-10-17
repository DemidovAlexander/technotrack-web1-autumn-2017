from django.shortcuts import render


def personalities(request, list_id=None):
    return render(request, 'personalities.html', {'list_id': list_id})


def personality(request, post_id=-1):
    return render(request, 'personality.html', {'post_id': post_id})
