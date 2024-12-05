from django.shortcuts import render
from django.http import HttpResponse
from django_user_agents.utils import get_user_agent

def index(request):
    user_agent = get_user_agent(request)
    is_mobile = user_agent.is_mobile  # Verdadero si es un móvil
    is_tablet = user_agent.is_tablet  # Verdadero si es una tablet
    is_pc = user_agent.is_pc          # Verdadero si es un computador

    # Pasa esta información al template
    return render(request, 'index.html', {
        'is_mobile': is_mobile,
        'is_pc': is_pc,
        'is_tablet': is_tablet,
    })