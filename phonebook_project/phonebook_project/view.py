from django.shortcuts import render, redirect, get_object_or_404
from .model import Contact
from .form import ContactForm

def add_record(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_records')
    else:
        form = ContactForm()
    return render(request, 'add_record.html', {'form': form})

def list_records(request):
    contacts = Contact.objects.all()
    return render(request, 'list_records.html', {'contacts': contacts})

def edit_record(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('list_records')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_record.html', {'form': form})

def delete_record(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('list_records')

def search_record(request):
    query = request.GET.get('query')
    if query:
        contacts = Contact.objects.filter(name__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'search_record.html', {'contacts': contacts})
