from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewUSerForm
from django.shortcuts import render,redirect

# Create your views here.
@login_required
def Home(request):
    Usuario = User.objects.get(username = request.user.username)
    context = {'Usuario':Usuario}
    return render(request,'index.html',context)

def Registro(request):
    if request.method == 'POST':
        form = NewUSerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = NewUSerForm()
    return render(request, 'registro.html', { 'form': form })