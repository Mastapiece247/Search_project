from django.shortcuts import render
from .models import Document

# Create your views here.


def search(request):
    query = request.GET.get("q")
    if query:
        results = Document.objects.filter(content__icontains=query)
    else:
        results = Document.objects.none()

    return render(
        request, "search_app/search_results.html", {"results": results, "query": query}
    )
