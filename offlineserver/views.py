from django.shortcuts import render
from django.views import View
from rest_framework.response import Response


class DataAPI(View):
    def get(self, request):
        message = "Hello, World!"
        return render(request, 'simple_temp.html', {'message': message})

    def post(self, request):
        data_received = request.POST.get('data', 'aniket singh') 
        return render(request, 'simple_temp.html', {'message': data_received})
