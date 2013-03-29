# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from django.dispatch import receiver

from djeventstream.signals import event_received

@csrf_exempt
def http_view(request):
    ''' This is a view which handles messages sent by a Django logging
    framework HttpHandler and dispatches them to Django signals. To
    subscribe, write a function similar to: 

    @receiver(djeventstream.signals.event_received)
    def f(sender, **kwargs):
       print kwargs['msg']

    '''
    if request.GET:
        try: # Not sure why this is necessary, but on some systems it is 'msg', and on others, 'message'
            message = request.GET['message']
        except MultiValueDictKeyError:
            message = request.GET['msg']
    else:
        try:
            message = request.POST['message']
        except:
            message = request.POST['msg']

    event_received.send(sender = http_view, msg = message)

    return HttpResponse( "Success" )

# uncomment/import for testing. 
# 
# @receiver(event_received)
# def f(sender, **kwargs):
#     print kwargs['msg']
