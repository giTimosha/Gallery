from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo, Comments


class IndexView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photo'

    def get_queryset(self):
        return Photo.objects.all()


class PhotoDetailView(DetailView):
    template_name = 'product/detail.html'
    model = Photo
    context_object_name = 'detail'

    def get_context_data(self, *, object_list=None, **kwargs):
        cont = super().get_context_data(object_list=object_list, **kwargs)
        cont['Comments'] = Comments.objects.all()
        return cont


class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'product/create.html'
    form_class = PhotoForm
    success_url = reverse_lazy('webapp:index')
    # permission_required = 'webapp.add_product'
    # permission_denied_message = '403 Доступ запрещён!'


class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'product/update.html'
    # form_class = PhotoForm
    fields = ('pictures', 'text')
    context_object_name = 'update'

    def get_success_url(self):
        return reverse('webapp:detail', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'delete'

    def delete(self, request, *args, **kwargs):
        photo = self.object = self.get_object()
        photo.delete()
        return HttpResponseRedirect(self.get_success_url())
