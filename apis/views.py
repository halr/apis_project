import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics

from apis.forms import LogMessageForm
from apis.models import LogMessage
from .models import Thing
from .serializers import ThingSerializer

# Create your views here.
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

class ListThingsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

def hello_there(request, name):
    return render(
        request,
        'apis/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    # return HttpResponse("Hello, Django!")
    return render(request, "apis/about.html")

def contact(request):
    return render(request, "apis/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now() # add TimeZone support
            # RuntimeWarning: DateTimeField LogMessage.log_date 
            # received a naive datetime (2020-05-27 22:47:32.945242) while time zone support is active.
            message.save()
            return redirect("home")
    else:
        return render(request, "apis/log_message.html", {"form": form})