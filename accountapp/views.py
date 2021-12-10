from django.http import HttpResponse
from django.shortcuts import render
from accountapp.models import NewModel


def hello_world(request):
    # return HttpResponse('Hello World!')
    if request.method == "POST":
        input_data = request.POST.get('input_data')
        new_model = NewModel()
        new_model.text = input_data
        new_model.save()
        return render(request, 'accountapp/hello_world.html', context={'new_model':new_model})
    return render(request, 'accountapp/hello_world.html')