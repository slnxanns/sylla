from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .forms import DocumentForm
from django.contrib.auth import get_user_model
from .forms import RegistrationForm 
from django.contrib.auth.decorators import login_required, user_passes_test

User = get_user_model()

##########################################################################################

# Restrict access to Author role
def is_author():
    return User.role == CustomUser.AUTHOR

# Restrict access to Collaborator role
def is_collaborator():
    return User.role == CustomUser.COLLABORATOR

##########################################################################################

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'cloudbook_app/document_list.html', {'documents': documents})

def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'cloudbook_app/document_form.html', {'form': form})

def edit_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'cloudbook_app/document_form.html', {'form': form})

def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'cloudbook_app/document_confirm_delete.html', {'document': document})

##########################################################################################

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a user object
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            
            # Assign a role based on form input, or any other criteria
            if form.cleaned_data['is_author']:
                user.role = User.AUTHOR
            else:
                user.role = User.COLLABORATOR
            
            user.save()

            # You can also assign the user to specific user groups here
            if form.cleaned_data['is_author']:
                user.groups.add(author_group)
            else:
                user.groups.add(collaborator_group)

            # Redirect to a success page or login page
            return redirect('login')  # You may need to adjust this URL

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
