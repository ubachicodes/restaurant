from django.shortcuts import render, redirect  # Add redirect import

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to database)
            form.save()
            return redirect('success')  # Redirect to the 'success' URL after successful form submission
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})
