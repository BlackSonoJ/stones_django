from django.shortcuts import render
from .models import Header, Service, Material


def landing(request):
    header = Header.objects.first()
    services = Service.objects.all()
    materials = Material.objects.all()
    return render(
        request,
        "index.html",
        {
            "header": header,
            "services": services,
            "materials": materials,
        },
    )
