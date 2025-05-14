from django.shortcuts import render
from django.http import HttpResponse
from .models import Genders

# Create your views here.
def add_gender(request):
    try:
        if request.method == 'post':
            gender= request.POSTg.get('gender')
            Genders.objects.create(gender=gender).save()
            return HttpResponse('gender added successfully!')
        else:
            return render(request, 'gender/AddGender.html')
    except Exception as e:
        return HttpResponse(f'Error occurred during add gender:{e}')