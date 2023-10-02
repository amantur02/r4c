from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from .serializers import OrderSerializer
import json


@method_decorator(csrf_exempt, name='dispatch')
class OrderCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            order = Order.objects.create(
                model=data['model'],
                version=data['version'],
                created=data['created']
            )
            serialized_order = OrderSerializer(order).data()
            return JsonResponse({'order': serialized_order}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
