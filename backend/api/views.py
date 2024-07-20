from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def get_name(request):
    return JsonResponse({"message": "Heng Yao"})

def get_degree(request):
    return JsonResponse({"message": "PhD in Computer Science"})
