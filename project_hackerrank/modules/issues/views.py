from django.shortcuts import render

from rest_framework.views import APIView #CLases basadas en Vistas
from rest_framework import status #Status COde HTTP
from rest_framework.response import Response # Return Json

from .models import Problemas
from modules.issues.serializers import ProblemasModelSerializer
from django.http import Http404
import random, requests
from modules.issues import functions

def index(request):
    return render(request,'index.html',{"title" : "Welcome","contents" : "Contenido"})

def activities_issues(request):
    id = random.randint(1,10)
    r = requests.get("http://127.0.0.1:8000/api/v1/issues/%s" % id)
    return render(request,'activities.html',{"title" : id,"contents" : r.json})

def result(request):
    r = request.POST
    if r['id_issue'] == '1':
        if functions.numeros_primos(r['textarea1']) is not False:
            return render(request,'success.html',{"title" : "Welcome","contents" : r['textarea1'] })
        
    if r['id_issue'] == '2':
        if functions.area_triangulo(r['textarea1']) is not False:
            return render(request,'success.html',{"title" : "Welcome","contents" : r['textarea1'] })
        
    if r['id_issue'] == '3':
        if functions.respuesta_usuario(r['textarea1']) is not False:
            return render(request,'success.html',{"title" : "Welcome","contents" : r['textarea1'] })
    
    if r['id_issue'] == '4':
        if functions.palindromos(r['textarea1']) is not False:
            return render(request,'success.html',{"title" : "Welcome","contents" : r['textarea1'] })
        
    if r['id_issue'] == '5':
        if functions.siguiente_viaje(r['textarea1']) is not False:
            return render(request,'success.html',{"title" : "Welcome","contents" : r['textarea1'] })
    
    if r['id_issue'] == '6':
        if functions.vasitos_necesarios(r['textarea1']) is not False:
            return render(request,'success.html',{"title" : "Welcome","contents" : r['textarea1'] })
        
    if r['id_issue'] == '7':
        if functions.agua_evaporada(r['textarea1']) is not False:
            return render(request,'success.html',{"title" : "Welcome","contents" : r['textarea1'] })
    
    if r['id_issue'] == '8':
        if functions.sentido_vida(r['textarea1']) is not False:
            #https://es.wikipedia.org/wiki/El_sentido_de_la_vida,_el_universo_y_todo_lo_dem%C3%A1s
            return render(request,'success.html',{"title" : "Welcome","contents" : r['textarea1'] })
    
    if r['id_issue'] == '9':
        if functions.hora_en_bucarest(r['textarea1']) is not False:
            return render(request,'success.html',{"title" : "Welcome","contents" : r['textarea1'] })
        
    if r['id_issue'] == '10':
        if functions.matriz(r['textarea1']) is not False:
            return render(request,'success.html',{"title" : "Welcome","contents" : r['textarea1'] })
    
    return render(request,'results.html',{"title" : "Welcome","contents" : r['textarea1'] })

class ListIssues(APIView):
    def get(self, request):
        problemas = Problemas.objects.filter()
        serializer = ProblemasModelSerializer(problemas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProblemasModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DetailIssues(APIView):
    def _get_issues(self, id):
        try:
            problemas = Problemas.objects.get(id=id)
            return problemas
        except Problemas.DoesNotExist:
            raise Http404

    def get(self, request,id):
        problemas = self._get_issues(id)
        serializer = ProblemasModelSerializer(problemas)
        return Response(serializer.data, status=status.HTTP_200_OK)
