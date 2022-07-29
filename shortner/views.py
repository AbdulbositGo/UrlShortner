from django.shortcuts import render, redirect
from django.http import HttpResponse
from uuid import uuid4
from .models import URL


# Create your views here.

def home(request):
    return render(request, 'index.html')


def create(request):

    if request.method == 'POST':
        print('salom')
        link = request.POST.get('link')
        if link[:8] != 'https://':
            link = "https://" + link
        old_link = URL.objects.filter(link=link).first()
        if old_link:
            return HttpResponse(old_link.uuid)
        else:
            uuid = str(uuid4())[:5]
            new_url = URL.objects.create(link=link, uuid=uuid)
            new_url.save()
            return HttpResponse(new_url.uuid)


def go(request, pk):
    url_details = URL.objects.filter(uuid=pk).first()
    if url_details:
        return redirect(url_details.link)
