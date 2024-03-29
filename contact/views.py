from django.shortcuts import render
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to database)
            form.save()
            return render(request, 'success.html')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})

