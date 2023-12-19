from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

challenges = {
    "January": "New year, new adventures!",
    "February": "The month of love and chilly winds.",
    "March": "Spring is in the air, time for new beginnings.",
    "April": "April showers bring May flowers.",
    "May": "Blooming flowers and warmer days ahead.",
    "June": "Summer vibes and sunshine all around.",
    "July": "Fireworks and barbecues, the essence of July.",
    "August": "Lazy summer days and ice cream cones.",
    "September": "Back-to-school and the beginning of fall.",
    "October": "Spooky season and pumpkin spice everything.",
    "November": "Gratitude and the warmth of family gatherings.",
    "December": "Festive lights and holiday cheer everywhere."
}


def index(request): 
    months = list(challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })


def monthly_challenge(request, month): 
    try:
        return render(request, 'challenges/challenge.html', {
            'title': month,
            'text': challenges[month]
        })
        challenge_text = challenges[month]
        return HttpResponse(challenge_text)
    except: 
        raise Http404("This month does not exist ")
    

def monthly_challenge_by_int(request, month): 
    
    if month > 12: 
        raise Http404("This month does not exist ")
    
    months = list(challenges.keys())
    url = reverse('monthly-challenge', args=[months[month-1]])
    return HttpResponseRedirect(url)
