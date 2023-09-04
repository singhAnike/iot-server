from django.shortcuts import render
from django.views import View

class DataAPI(View):
    def get(self, request):
        message = "Hello, World!"
        data_received = request.GET.get('data', None)
        return render(request, 'form.html', {'message': message, 'data_received': data_received})

    def post(self, request):
        data_received = request.POST.get('data', None)
        message = "Data submitted successfully"
        return render(request, 'form.html', {'message': message, 'data_received': data_received})
