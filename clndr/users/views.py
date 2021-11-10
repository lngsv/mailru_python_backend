from django.http.response import JsonResponse
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods

from users.models import User


@require_http_methods(['POST'])
def create_user(request):
    res = User.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            username=request.POST.get('username'),
    )
    return JsonResponse({'id': res.id})


@require_http_methods(['GET'])
def user_details(request, user_id):
    try:
        found_user = User.objects.get(id=user_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound('User not found')
    return JsonResponse(dict(
        id=found_user.id,
        username=found_user.username,
        first_name=found_user.first_name,
        last_name=found_user.last_name,
        email=found_user.email,
    ))


@require_http_methods(['GET'])
def user_list(request):
    return JsonResponse({
        'users': [dict(
            id=u.id,
            username=u.username,
        ) for u in User.objects.all()],
    })
