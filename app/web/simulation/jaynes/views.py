import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from .simulator.jaynes import createJaynesModel, vaccumRabiOscillations, wignerFunctions

# APIs
def index(request):
    template = loader.get_template('jaynes/base.html')
    return HttpResponse(template.render())

@method_decorator(csrf_exempt, name='dispatch')
class Rabi(TemplateView):
    def get(self, request, *args, **kwargs):
        template = loader.get_template('jaynes/rabi.html')
        return HttpResponse(template.render())
    
    def post(self, request, *args, **kwargs):
        print("Fetching Rabi frequency graph")
        config = dict(list(request.POST.items())[:-4])
        config["no_of_cavity_states"] = "15"
        config["no_of_atom_states"] = "2"
        print(config)
        model = createJaynesModel(config)
        # print(model)

        # config = dict(list(request.POST.items())[-4:])
        # print("System: ",config)

        rabi_labels, rabi_data_cavity,rabi_data_atom  = vaccumRabiOscillations(model, float(config['t']), int(config['no_t']))

        response = {
            'labels': list(rabi_labels),
            'data_cavity': list(rabi_data_cavity),
            'data_atom': list(rabi_data_atom),
        }

        print(response)

        return JsonResponse(data=response)

@method_decorator(csrf_exempt, name='dispatch')
class Wigner(TemplateView):
    def get(self, request, *args, **kwargs):
        template = loader.get_template('jaynes/wigner.html')
        return HttpResponse(template.render())

    def post(self, request, *args, **kwargs):
        print("Fetching Wigner function graph")
        config = request.POST.dict()
        print(request.POST)
        config["tinterest"] = request.POST.getlist('tinterest[]')
        print(config)
        # config = dict(list(request.POST.items()))
        config["no_of_cavity_states"] = "15"
        config["no_of_atom_states"] = "2"
        print(config)
        model = createJaynesModel(config)

        # config = dict(list(request.POST.items())[-4:])
        # print("System: ",config)
        # tinterest = [0.0, 5.0, 15.0, 25.0]

        tint, wigner_label, wigner_data = wignerFunctions(model, -float(config['x']), float(config['x']), int(config['no_x']),float(config['t']), int(config['no_t']), [float(strtinterest) for strtinterest in config["tinterest"]] )
        
        response = {
            'time': list(tint),
            'labels': list(wigner_label),
            'wigner_data': wigner_data,
        }
        # print(response)

        return JsonResponse(data=response)