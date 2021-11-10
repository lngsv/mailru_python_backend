from datetime import datetime

from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods

from events.models import Event


# DATETIME_FORMAT = '%Y-%m-%d %H:%M'


@require_http_methods(['POST'])
def create_event(request):
    res = Event.objects.create(
            name=request.POST.get('name'),
            from_date=request.POST.get('from_date'),
            to_date=request.POST.get('to_date'),
            comment=request.POST.get('comment'),
            creator_id=request.POST.get('creator_id'),
    )
    return JsonResponse({'created': res.id})


@require_http_methods(['GET'])
def event_details(request, event_id):
    try:
        found_event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound('Event not found')
    return JsonResponse(model_to_dict(found_event))


@require_http_methods(['GET'])
def event_list(request):
    return JsonResponse({
        'events': [model_to_dict(e) for e in Event.objects.all()],
    })


@require_http_methods(['POST'])
def update_event(request, event_id):
    try:
        found_event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound('Event not found')

    if 'name' in request.POST:
        found_event.name = request.POST['name']
    if 'comment' in request.POST:
        found_event.comment = request.POST['comment']
    if 'from_date' in request.POST:
        found_event.from_date = request.POST['from_date']
    if 'to_date' in request.POST:
        found_event.to_date = request.POST['to_date']


    found_event.save()
    return JsonResponse({'updated': event_id})


@require_http_methods(['POST'])
def delete_event(request, event_id):
    try:
        found_event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound('Event not found')

    Event.objects.filter(id=event_id).delete()
    return JsonResponse({'deleted': event_id})

