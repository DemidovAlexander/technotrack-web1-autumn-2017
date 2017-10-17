from django.shortcuts import render


def references(request, list_id=-1):
    return render(request, 'references.html', {'list_id': list_id})


def reference(request, post_id=-1):
    return render(request, 'reference.html', {'post_id': post_id})
