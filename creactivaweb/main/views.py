from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View

class IndexView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request):
        return render(request, 'index.html')
    
# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'registration/register.html')

	# acá viene la función post del formulario de registro
