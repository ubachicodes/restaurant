from .forms import ReserveForm
from django.shortcuts import render
from django.http import JsonResponse

def reservation(request):
    reservation_form = ReserveForm()

    if request.method == 'POST':
        reservation_form = ReserveForm(request.POST)
        
        if reservation_form.is_valid():
            reservation_form.save()
        else:
            # Form is not valid, handle the error case
            context = {'form': reservation_form}
            return render(request, 'reservation/reservation.html', context)

    context = {'form': reservation_form}
    return render(request, 'reservation/reservation.html', context)

def tables_api(request):
    if request.method == 'GET':
        # Get parameters from the request
        date = request.GET.get('date')
        time = request.GET.get('time')
        
        # Process the request data (e.g., query the database)
        # Perform actions based on the data
        
        # Generate a response (e.g., return JSON data)
        response_data = {
            'date': date,
            'time': time,
            'tables_available': 10  
        }
        return JsonResponse(response_data)
    else:
        # Handle unsupported request methods
        return JsonResponse({'error': 'Method not allowed'}, status=405)
