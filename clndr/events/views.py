from dataclasses import asdict

# from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods

from events.models import Event, EVENTS_DB


@require_http_methods(['POST'])
def create_event(request):
    event_id = len(EVENTS_DB)
    EVENTS_DB[event_id] = Event(
            event_id,
            request.POST.get('name'),
            request.POST.get('from_date'),
            request.POST.get('to_date'),
            request.POST.get('comment'),
    )
    return JsonResponse({'id': event_id})


@require_http_methods(['GET'])
def event_details(request):
    try:
        event_id = int(request.GET['id'])
    except (KeyError, ValueError):
        actual_event_id = request.GET.get('id')
        return HttpResponseBadRequest(
                f'Integer id expected, \"{actual_event_id}\" got'
        )
    found_event = EVENTS_DB.get(event_id)
    if found_event is None:
        return HttpResponseNotFound('Event not found')
    return JsonResponse(asdict(found_event))


@require_http_methods(['GET'])
def event_list(request):
    return JsonResponse({
        'events': [asdict(e) for e in EVENTS_DB.values()]
    })
