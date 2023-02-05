from typing import Any, Dict
from django.http import HttpRequest, JsonResponse
from django.forms.models import model_to_dict
from products.models import Product
import json

def api_home(request: HttpRequest, *args, **kwargs):
    data= Product.objects.all().order_by("?").first()
    result={}
    if data:
        result = model_to_dict(data, fields=['id', 'title'])
    return JsonResponse(result)