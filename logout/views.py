from django.shortcuts import render
from . models import Logout

# Create your views here.
def logout(request):
    about = Logout.objects.all()
    return render(request, 'logout.html',{"about":about})
