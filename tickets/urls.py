from django.urls import path
from django.views.generic import RedirectView

from .views import WelcomeView, GetTicket, ChangeOilView, InflateTires, Diagnostic, ProcessingView, NextView

urlpatterns = [
    path('welcome/', WelcomeView.as_view()),
    path('menu/', GetTicket.as_view()),
    path('get_ticket/change_oil', ChangeOilView.as_view()),
    path('get_ticket/inflate_tires', InflateTires.as_view()),
    path('get_ticket/diagnostic', Diagnostic.as_view()),
    path('processing', ProcessingView.as_view()),
    path('processing/', RedirectView.as_view(url='/processing')),
    path('next', NextView.as_view())

]