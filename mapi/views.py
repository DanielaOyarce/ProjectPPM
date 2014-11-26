from django.db.models import Q
from django.shortcuts import render_to_response
from models import Book
from forms import ContactForm
 
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("books/search.html", {
        "results": results,
        "query": query
    })
 
def contact(request):
    form = ContactForm()
    return render_to_response('contact.html', {'form': form})