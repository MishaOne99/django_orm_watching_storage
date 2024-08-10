from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    
    non_closed_visits = []
    
    for visit in visits:
        name = visit.passcard.owner_name
        
        total_seconds = visit.get_duration()
        time_visit = visit.format_duration(total_seconds)
        
        result = {
            'who_entered': name,
            'entered_at': visit.entered_at,
            'duration': time_visit
        }
        
        non_closed_visits.append(result)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
