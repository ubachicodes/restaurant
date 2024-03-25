from .models import Reservation
from django.shortcuts import render
from .forms import ReserveForm

from reservation.models import Reservation

def reservation(request):
    reservation_form = ReserveForm()

    if request.method == 'POST':
        reservation_form = ReserveForm(request.method)
        
        
        if reservation_form.is_valid():
            reservation_form.save()

    context = {'form':reservation_form}

    return render(request, 'reservation/reservation.html', context)
     
        
    