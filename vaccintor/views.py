from django.shortcuts import render
from django.http import HttpResponse
from .models import Parent, Vaccine, Child, VaccineCompletion
from .logic import send_text
# Create your views here.
def hello(request):
    return HttpResponse("WELCOME TO MY WEBSITE")


def check_children_status(request):
    parents = Parent.objects.all()
    # Wow we should get rid of all these loops so the Database doesn't get ruined
    for parent in parents:
        reminders = []
        children = parent.children.all()
        d = {}
        for child in children:
            due_today = []
            overdue = []
            coming_up = []
            vaccine_checks = VaccineCompletion.objects.filter(child=child)
            for vc in vaccine_checks:
                if not vc.completed:
                    if vc.needed:
                        if vc.days_until_needed == 0:
                            due_today.append(vc.vaccine.simple_name)
                        if vc.days_until_needed < 0:
                            overdue.append([vc.vaccine.simple_name, vc.days_until_needed])
                    else:
                        if vc.days_until_needed < 5:
                            coming_up.append([vc.vaccine.simple_name, vc.days_until_needed])
            d[child.full_name] = [due_today, overdue, coming_up]
        message = "You have some new vaccinations coming up for your kids: {}".format(str(d))
        send_text(str(parent.phone_number), message)
    return HttpResponse("Checked")