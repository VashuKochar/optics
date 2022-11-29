from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .model.model import vaccumRabiOscillations, wignerFunctions

# Helper functions
# def constructModel(request):
#     model = {
#         "atomic_frequency" : request.val(),
#         # atomic_dissipation : $("#atomic_dissipation").val(),
#         # atomic_initial : $("input[name='atomic_initial']:checked").val(),
#         # cavity_frequency : $("#cavity_frequency").val(),
#         # cavity_dissipation : $("#cavity_dissipation").val(),
#         # cavity_initial : $( "#cavity_initial").val(),
#         # coupling : $("#coupling").val(),
#         # thermal : $("#thermal").val(),
#         # rwa : $("#rwa").val(),
#         # x : $("#x").val(),
#         # no_x : $("#no_x").val(),
#         # t : $("#t").val(),
#         # no_t : $("#no_t").val(),
#     }
#     return model

# APIs
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

@csrf_exempt
def rabi(request):
    print("Fetching Rabi frequency graph")
    model = request.POST
    
    print(model)
    return HttpResponse("Rabi")

@csrf_exempt
def wigner(request):
    print("Fetching Wigner function graph")
    model = request.POST

    print(model)
    return HttpResponse("Wigner")