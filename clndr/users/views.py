from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods

from users.models import User, USERS_DB


@require_http_methods(['POST'])
def create_user(request):
    user_id = len(USERS_DB)
    USERS_DB[user_id] = User(
            user_id,
            request.POST.get('name'),
            request.POST.get('login'),
    )
    print(request.POST)
    return JsonResponse({'id': user_id})


@require_http_methods(['GET'])
def user_details(request):
    try:
        user_id = int(request.GET['id'])
    except (KeyError, ValueError):
        actual_user_id = request.GET.get('id')
        return HttpResponseBadRequest(
                f'Integer id expected, \"{actual_user_id}\" got'
        )
    found_user = USERS_DB.get(user_id)
    if found_user is None:
        return HttpResponseNotFound('User not found')
    return JsonResponse(model_to_dict(found_user))


@require_http_methods(['GET'])
def user_list(request):
    return JsonResponse({'users': [model_to_dict(u) for u in USERS_DB.values()]})
