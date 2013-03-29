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