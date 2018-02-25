from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Category,Location

# Create your views here.
def home (request):
    
    images = Image.get_images()
    return render(request,'home.html',
                  {"images":images})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_category(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"categories":searched_category})

    else:
        message = "You havent searched any category"
        return render(request,'search.html',{"message":message})

def image(request,image_id):
    try:
        image=Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'image.html',{"image":image})

def filter_location(request,id):
    images= Image.filter_by_location(id= location.id)
    return render(request,'filter.html',{"images":images})
