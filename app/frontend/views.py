from django.shortcuts import render, redirect, get_object_or_404

from files.forms import CodeFileForm
from reports.models import Report


# Create your views here.


def home(request):

    if request.method == 'POST':
        form = CodeFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('frontend:home')
    else:
        form = CodeFileForm()
    context = {
        'form': form
    }
    return render(request, template_name='pages/home.html', context=context)


def report(request, file_uid):
    context = {
        "report": get_object_or_404(Report, pk=file_uid)
    }
    return render(request, template_name='pages/report.html', context=context)
