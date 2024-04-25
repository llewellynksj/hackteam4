from django.http import HttpResponse


def team(request):
    return HttpResponse("Hello, world. You're at the team page.")
