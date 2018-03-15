from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from trilateration import trelaterate, get_distance

from qsstats import QuerySetStats


from .models import Unit

from django.views.generic import TemplateView


class UnitPageView(TemplateView):
    model = Unit
    template_name = 'unit.html'

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
    data = []
    if request.method == 'POST':
        print(request.POST['data'])
        str_data = request.POST['data']
        data = [list(map(int, i.split(','))) for i in str_data.split(';')]

    # get distance from beacons
    dists_raw = [0]*len(data)
    beacs = [0]*len(data)
    for i in range(len(data)):
        dists_raw[i] = get_distance(data[i][1], data[i][2])
        beacs[i] = data[i][0]

    indces = sorted(range(len(dists_raw)), key=lambda k: dists_raw[k])

    dists_3_best = [0]*3
    for i in range(len(dists_3_best)):
        j = indces[i]
        dists_3_best[i] = (beacs[j], dists_raw[j])

    # Beacons table
    with open('data', 'w') as f:
        f.write(str(trelaterate(dists_3_best)))

    return HttpResponse(status=201)

@csrf_exempt
def coords(request):
    s=''
    if request.method == 'GET':
        # Beacons table
        with open('data', 'r') as f:
            s = f.readline()

    return HttpResponse(s, content_type="text/plain", status=200)
    print(s)
