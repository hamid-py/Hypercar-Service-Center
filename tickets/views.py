from django.shortcuts import HttpResponse, render, redirect
from django.views import View

car_line = {'ticket_number': 0, 'change_oil': [], 'inflate_tires': [], 'diagnostic': []}
next_ticket_list = [None]


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class GetTicket(View):
    def get(self, request, *args, **kwargs):
        ticket_list = ['Change oil', 'Inflate tires']
        return render(request, 'tickets\get_ticket.html', context={'ticket': ticket_list})


class ChangeOilView(View):
    def get(self, request, *args, **kwargs):
        wait_time = len(car_line['change_oil']) * 2
        car_line['ticket_number'] += 1
        car_line['change_oil'].append(car_line['ticket_number'])
        ticket_number = car_line['change_oil'][-1]
        return render(request, 'tickets\\ticket.html',
                      context={'ticket_number': ticket_number, 'wait_time': wait_time})


class InflateTires(View):
    def get(self, request, *args, **kwargs):
        wait_time = len(car_line['change_oil']) * 2 + len(car_line['inflate_tires']) * 5
        car_line['ticket_number'] += 1
        car_line['inflate_tires'].append(car_line['ticket_number'])
        ticket_number = car_line['inflate_tires'][-1]
        return render(request, 'tickets\\ticket.html',
                      context={'ticket_number': ticket_number, 'wait_time': wait_time})


class Diagnostic(View):
    def get(self, request, *args, **kwargs):
        wait_time = len(car_line['change_oil']) * 2 + len(car_line['inflate_tires']) * 5 + \
                    len(car_line['diagnostic'] * 30)
        car_line['ticket_number'] += 1
        car_line['diagnostic'].append(car_line['ticket_number'])
        ticket_number = car_line['diagnostic'][-1]
        return render(request, 'tickets\\ticket.html',
                      context={'ticket_number': ticket_number, 'wait_time': wait_time})


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tickets\process.html', context={'car_line': car_line})

    def post(self, request, *args, **kwargs):
        if car_line['change_oil']:
            next_ticket_list[0] = car_line['change_oil'].pop(0)
        elif car_line['inflate_tires']:
            next_ticket_list[0] = car_line['inflate_tires'].pop(0)
        elif car_line['diagnostic']:
            next_ticket_list[0] = car_line['diagnostic'].pop(0)
        else:
            next_ticket_list[0] = None
        return redirect('/next')


class NextView(View):
    def get(self, request, *args, **kwargs):
        if next_ticket_list[0]:
            next_ticket = next_ticket_list[0]
        else:
            next_ticket = None
        return render(request, 'tickets/next.html', context={'next_ticket': next_ticket})
