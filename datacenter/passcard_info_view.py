from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


STAY_DURATION = 3600


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = []
    
    visits = Visit.objects.filter(passcard=passcard)
    
    for visit in visits:
        total_seconds = visit.get_duration()
        
        result = {
            'entered_at': visit.entered_at, 
            'duration': visit.format_duration(total_seconds),
            'is_strange': total_seconds > STAY_DURATION
        }
        this_passcard_visits.append(result)
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
