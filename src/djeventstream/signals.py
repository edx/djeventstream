import django.dispatch

event_received = django.dispatch.Signal(providing_args = ["msg"] )
