from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView


from .models import PictureAlbum
def gallery(request):
    pictures = PictureAlbum.objects.all().order_by('-created')
    Paginator = Paginator(list, 10)
    page =request.get('Page')
    try:
        picturealbums = Paginator.page(page)
    except PageNotAnInteger:
        picturealbums = Paginator.page(1)
    except EmptyPage:
        picturealbums = paginator.page(paginator.num_pages)
    return render(request,'gallery.html', {'picturealbums':pictures})


class picturedetail(DetailView):
    model = PictureAlbum
    def get_context_data(self, **kwargs):
        context = super(picturedetail, self).get_context_data(**kwargs)

        context['images'] = picturedetailimage.objects.filter(album=self.object.id)
        retur context