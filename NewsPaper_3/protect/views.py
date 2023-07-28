ffrom django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def protected_view(request):
    return render(request, 'protected_view.html')

