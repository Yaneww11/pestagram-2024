from django.shortcuts import render, redirect
from common.forms import CommentForm
from photos.forms import PhotoCreateForm, PhotoEditForm
from photos.models import Photo


def photo_add_page(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            form.save()
            return redirect('home-page')

    context = {
        'form' : form,
    }

    return render(request, 'photos/photo-add-page.html', context)

def photo_edit_page(request, pk:int):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk=pk)

    context = {
        'form' : form,
        'photo' : photo
    }

    return render(request, 'photos/photo-edit-page.html', context)

def photo_detail_page(request, pk:int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    comment_form = CommentForm()

    context = {
        'photo' : photo,
        'like' : likes,
        'comments' : comments,
        'comment_form' : comment_form
    }

    return render(request, 'photos/photo-details-page.html', context)

def photo_delete(request, pk: int):
    photo = Photo.objects.get(pk=pk).delete()
    return redirect('home-page')