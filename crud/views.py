from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crudapp.models import log

class logForm(ModelForm):
    class Meta:
        model = log
        fields = ['name', 'pages']

def log_list(request, template_name='log/log_list.html'):
    Log = log.objects.all()
    data = {}
    data['object_list'] = Log
    print(log)
    return render(request, template_name, data)

def log_view(request, pk, template_name='log/log_view.html'):
    Log= get_object_or_404(log, pk=pk)
    return render(request, template_name, {'object':Log})

def log_create(request, template_name='log/log_form.html'):
    form = logForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('log_view')
    return render(request, template_name, {'form':form})

def log_update(request, pk, template_name='log/log_form.html'):
    Log= get_object_or_404(Book, pk=pk)
    form = logForm(request.POST or None, instance=Log)
    if form.is_valid():
        form.save()
        return redirect('log_list')
    return render(request, template_name, {'form':form})

def log_delete(request, pk, template_name='log/logdelete.html'):
    Log = get_object_or_404(log, pk=pk)
    if request.method=='POST':
        Log.delete()
        return redirect('log_list')
    return render(request, template_name, {'object':Log})