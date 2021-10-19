from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from code_challenge.utils import powerplant


# Create your views here.
@csrf_exempt
def power_supply(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if data is not None:
            try:
                powerplant_utils = powerplant(data)
                powerplants = powerplant_utils.order_powerplants(data['powerplants'])
                power = powerplant_utils.power(powerplants)
                return JsonResponse({'result': power},  status=status.HTTP_200_OK)
            except Exception as e:
                return JsonResponse({'error': e},  status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'status':'ERROR 400 BAD REQUEST'},  status=status.HTTP_400_BAD_REQUEST)
    
    return JsonResponse({'status':'ERROR 405 METHOD NOT ALLOWED'},  status=status.HTTP_405_METHOD_NOT_ALLOWED)