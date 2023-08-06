from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'listings/index.html')


def listing(request):
    return render(request, 'listings/listing.html')


def search(request, listing_id):
    return render(request, 'listings/search.html')
