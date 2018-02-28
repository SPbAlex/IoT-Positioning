from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from qsstats import QuerySetStats


from .models import Unit

from django.views.generic import TemplateView


class UnitPageView(TemplateView):
    model = Unit
    template_name = 'unit.html'

    from qsstats import QuerySetStats

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Unit.objects.all()
        return context


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


@csrf_exempt
def vote(request):
    print('Hello')
    if request.method == 'POST':
        print(request.POST['data'])
    return HttpResponse(status=201)
