from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse


# Create your views here.
class HomePageView(View):
    def get(self, request):

        template = loader.get_template('henrybookstore/home.html')        

        context = {
            'title': 'Henry Bookstore'
        }

        return HttpResponse(template.render(context, request))
    

