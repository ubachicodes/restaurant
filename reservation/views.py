from .forms import ReserveForm
from django.shortcuts import render

def reservation(request):
    reservation_form = ReserveForm()

    if request.method == 'POST':
        reservation_form = ReserveForm(request.POST)
        
        if reservation_form.is_valid():
            reservation_form.save()

    context = {'form': reservation_form}

    return render(request, 'reservation/reservation.html', context)
