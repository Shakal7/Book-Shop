from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def Home(request):
    books = book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'HTML/Home.html', context)


def upload_books(request):
    form = bookForm()

    if request.method == 'POST':
        form = bookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')

    context = {
        'form': form
    }
    return render(request, 'HTML/upload_book.html', context)


def delete_book(request, id):
    bk = book.objects.get(pk=id)
    if request.method == 'POST':
        bk.delete()
        return redirect('Home')
    context = {'bk': bk}

    return render(request, template_name='HTML/delete_book.html', context=context)


def update_book(request, id):
    b = book.objects.get(pk=id)
    form = bookForm(instance=b)
    if request.method == 'POST':
        form = bookForm(request.POST, request.FILES, instance=b)
        if form.is_valid():
            form.save()
            return redirect('Home')
    context = {'b': b}

    return render(request, template_name='HTML/delete_book.html', context=context)
