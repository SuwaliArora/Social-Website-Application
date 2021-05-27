from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required        # login_required	decorator to image_create view to prevent access for unauthenticated users
def image_create(request):
    if request.method == 'POST':
        #form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            #assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added succesfully')

            #redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        #build form with data provided by the bookmarklet vai GET
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})

#simple detail view to display an image that has saved into our site
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})

@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id') #id of image object on which user is performing action
    action = request.POST.get('action')  #action that user want to perform, assume to be a string with value like or unlike
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})    #jsonresponse provided by django, returns http response

@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8) #Paginator object to paginate the results
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        image = paginator.page(1)
    except EmptyPage:              #EmptyPage exception if requested page is out of range
        if request.is_ajax():
            #if the request is AJAX and the page is out of range
            #return an empty page
            return HttpResponse('')
        #if page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'images/image/list_ajax.html', {'section': 'images', 'images': images})
    return render(request, 'images/image/list.html', {'section': 'images', 'images': images})
    
