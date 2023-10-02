import json
from django.http import JsonResponse


def parse_and_validate_data(request, serializer):
    try:
        data = json.loads(request.body)
        validated_data = serializer(data)
        if not validated_data.is_valid():
            errors = validated_data.errors
            return JsonResponse({'error': errors}, status=400)
        return validated_data.validated_data
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
