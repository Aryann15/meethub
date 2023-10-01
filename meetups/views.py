from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    meetups = [
        {"title": "web3 meetup", "location": "Bengaluru", "slugs": "web3-meetup"},
        {"title": "ai meetup", "location": "delhi", "slugs": "ai-meetups"},
    ]
    return render(request, "meetups/index.html", {
        'meetups': meetups
    })
