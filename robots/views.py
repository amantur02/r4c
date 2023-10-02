import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core import serializers


from .models import Robot
from .forms import RobotCreateForm


@csrf_exempt
@require_POST
def create_robot(request):
    try:
        data = json.loads(request.body)
        form = RobotCreateForm(data)

        if form.is_valid():
            model = form.cleaned_data['model']
            version = form.cleaned_data['version']
            created = form.cleaned_data['created']

            # Check if a robot with the same serial number exists
            serial = f'{model}-{version}'
            if Robot.objects.filter(serial=serial).exists():
                return JsonResponse({'error': 'Robot with the same serial number already exists'}, status=400)

            # Create a new robot instance
            robot = Robot(
                model=model,
                version=version,
                created=created,
                serial=serial
            )
            robot.save()

            serialized_robot = serializers.serialize('json', [robot, ])

            return JsonResponse({'robot': serialized_robot}, status=201)
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'error': 'Invalid form data', 'errors': errors}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
