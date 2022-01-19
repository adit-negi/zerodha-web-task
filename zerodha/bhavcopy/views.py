from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse

# Create your views here.
def search_bhavcopy(request, name):
    keyword = name
    result = cache.get_many(cache.keys(keyword+"*"))
    result_dict = dict(result)
    values_list = list(result_dict.values())
    return JsonResponse(values_list, safe=False)

def home_page(request):
    return render(request,'bhavcopy/home.html')

def bhavcopy_all(request):
    result = cache.get_many(cache.keys("*"))
    result_dict = dict(result)
    values_list = list(result_dict.values())
    return JsonResponse(values_list, safe=False)