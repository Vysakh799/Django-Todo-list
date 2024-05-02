from django.shortcuts import render
import datetime
from .models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=='POST':
        x=datetime.datetime.now()
        date=(x.strftime("%x"))
        date_string = date

        try:
        # Split the string at "/"
            parts = date_string.split("/")

            # Assuming two-digit year, prepend "20"
            year = "20" + parts[2]

            # Create the formatted date string
            formatted_date = f"{year}-{parts[0]}-{parts[1]}"
        except IndexError:
             print("Invalid date format. Please use MM/DD/YY.")


        
        list=request.POST['list']
        try:
            data=todo.objects.get(list=list)
            print(data)
            return HttpResponse("list alreadt exist pls update it")
        except:
            pass
        data=todo.objects.create(date=formatted_date,list=list)
        data.save()
    data=todo.objects.all()
    return render(request,'index.html',{'data':data})
