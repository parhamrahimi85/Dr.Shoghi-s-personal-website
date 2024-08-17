from django.shortcuts import render, redirect

from .forms import UserForm
from .models import Vars


def variable_info_view(request):

    var_data = Vars.objects.all().first()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  # Redirect to success URL
    else:
        form = UserForm()

    context = {'var': var_data, 'form': form}
    return render(request, 'main/main.html', context)
