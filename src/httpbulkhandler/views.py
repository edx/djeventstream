# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from django.dispatch import receiver

from djeventstream.signals import event_received

@csrf_exempt
def http_bulk_view(request):
    ''' This is a view which handles messages sent by a Django logging
    framework HttpHandler and dispatches them to Django signals. To
    subscribe, write a function similar to: 

    @receiver(djeventstream.signals.event_received)
    def f(sender, **kwargs):
       print kwargs['msg']

    '''
    if False: # Useful code path, but untested
        message = False
        if 'message' in request.POST or 'msg' in request.POST:
            message = request.POST['message']
            message = request.POST['msg']
        if message: 
            event_received.send(sender = http_bulk_view, msg = message.split("\n"))
            #for line in message.split("\n"):
            #    event_received.send(sender = http_bulk_view, msg = message)
            return HttpResponse( "Success" )

    event_received.send(sender = http_bulk_view, msg = request.readlines())

    #for line in request.readlines():
    #    event_received.send(sender = http_bulk_view, msg = line)

    return HttpResponse( "Success" )

# uncomment/import for testing. 
# 
# @receiver(event_received)
# def f(sender, **kwargs):
#     print kwargs['msg']
