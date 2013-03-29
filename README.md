djeventstream
=============

This is a framework for receiving events sent by the Python logging
framework. It is the Django-based mate to loghandlersplus. It can take
events from a Python logging framework HTPPHandler, or a
loghandlersplus SNSHandler, and convert those to Django signals.

To use: 

    sudo pip install -e git+https://github.com/MITx/djeventstream#egg=djeventstream

Add the handler to INSTALLED_APPS in settings.py: 

    INSTALLED_APPS = (
        ...
        'djeventstream.httphandler',
        ...
    )


Add a view to urls.py: 

    url(r'^httpevent$', 'djeventstream.httphandler.views.http_view'),

To receive the events, add a Django receiver: 

    from djeventstream.signals import event_received
    from django.dispatch import receiver
    
    @receiver(event_received)
    def f(sender, **kwargs):
        print kwargs['msg']


One minor caveat: Be aware that Django loads many parts of an
application lazily (e.g. a view is loaded when it is first called). If
you don't want to lose events, make sure the receiver is placed
somewhere where it is imported on application startup. 

For SNS events, settings.py needs to contain one of two things: 

    SNS_PUBLIC = True

In this case, your application will handle SNS events from
anyone. This is primarily useful for debugging. For deployment, you
should explicitly list the ARNs you would like to accept subscriptions
from:

    SNS_PUBLIC = False
    SNS_SUBSCRIPTIONS = ["arn:aws:sns:us-east-2:1234567890:sns_arn"]

Please note that this framework does not, yet, verify signatures on
events. You cannot trust that that the events came from Amazon without
a secondary security mechanism (the same is true of the HTTP handler).