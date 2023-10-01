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


def meetup_details(request, meetup_slug):
    selected_meetup = {
     'title': 'web3 meetup' , 'description' : 'this is a web3 meetup!'   
    }
    return render(request ,'meetups/details.html',{
        'meetup_title' : selected_meetup["title"],
        'meetup-description' : selected_meetup['description']
    })