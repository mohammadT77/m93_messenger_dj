from django.http.response import JsonResponse
# Create your views here.

def index_view(req):
    data = {
        'message': "Hello world",
    }
    return JsonResponse(data)

# @csrf_exempt
# def index_post(req):
#     pass