from django.shortcuts import render
from app.forms import GalleryImageForm
from django.shortcuts import redirect
from app.models import PhotoGallery
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='account/login')
def index(request):
    user = request.user
    images = PhotoGallery.objects.filter(user_id=user.id)
    image_list = []
    for image in images:
        image_list.append({
            'id':image.id,
            'name':image.name,
            'img':image.image
        })
    page_number = request.GET.get('page')
    p = Paginator(image_list, 5)
    page_obj = p.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, "app/index.html", context)

@login_required(login_url='account/login')
def add_photo(request):
    user = request.user
    if request.method == 'GET':
        form = GalleryImageForm()
        return render(request, 'app/add_photo.html', {'form': form})
    else:
        request.POST._mutable = True
        request.POST["user_id"] = user.id
        request.POST["name"] = 'user.id'
        request.POST._mutable = True

        form = GalleryImageForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('/')