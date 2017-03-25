import subprocess

from django.contrib import messages
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        try:
            subprocess.check_call(['/usr/sbin/service', 'lxdm', 'restart'])
            messages.info(request, 'Kodi has been restarted')
        except (subprocess.CalledProcessError, OSError):
            messages.error(request, 'Something went wrong. You should probably email Ian for help.')

    return render(request, "index.html")
