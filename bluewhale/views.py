from django.shortcuts import render, redirect
from .models import Note


# HOME PAGE

def index(request):

    tasks = Note.objects.all()

    if request.method == 'POST':

        a = request.POST.get('title')

        b = request.POST.get('content')

        Note.objects.create(
            title=a,
            content=b
        )

        return redirect('/')

    return render(request, 'index.html', {'tasks':tasks})


# DELETE

def delete(request, id):

    note = Note.objects.get(id=id)

    note.delete()

    return redirect('/')


# UPDATE

def update(request, id):

    note = Note.objects.get(id=id)

    tasks = Note.objects.all()

    if request.method == 'POST':

        note.title = request.POST.get('title')

        note.content = request.POST.get('content')

        note.save()

        return redirect('/')

    return render(request, 'index.html', {
        'edit_note':note,
        'tasks':tasks
    })