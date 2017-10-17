from django.shortcuts import render


class BooksList(ListView):
    template_name = "core/user_page.html"
    model = Blog
    

def books(request, list_id=-1):
    return render(request, 'books.html', {'list_id': list_id})


def books_personality(request, post_id=-1):
    return render(request, 'books_personality.html', {'post_id': post_id})


def books_item(request, post_id=-1):
    return render(request, 'books_item.html', {'post_id': post_id})
