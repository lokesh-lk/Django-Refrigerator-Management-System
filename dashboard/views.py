from django import template
from django.contrib.auth import login
from django.forms import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse, response
from django.contrib.auth.decorators import login_required
from .models import Client, Inward, Dispatch
from .forms import InwardForm, ClientForm, DispatchForm
from django.contrib.auth.models import User
from django.contrib import messages
import datetime
import reportlab
#from .forms import InvoiceForm,OrderForm

from django.http import HttpResponse
from reportlab.pdfgen import canvas

from django.http import HttpResponse
from django.views.generic import View
 
from xhtml2pdf import pisa  

from django.template.loader import get_template
from .models import render_to_pdf 

#from django.views.generic import View
#from .models import render_to_pdf #created in step 4

# Create your views here.

@login_required
def index(request):
    dispatchs = Dispatch.objects.all()
    inwards = Inward.objects.all()
    dispatchs_count = dispatchs.count()
    inward_count = inwards.count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        form = DispatchForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = DispatchForm()
    
    context = {
        'dispatchs': dispatchs,
        'inwards': inwards,
        'dispatchs_count': dispatchs_count,
        'inward_count': inward_count,
        'workers_count': workers_count,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def client_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/client_detail.html', context)

@login_required
def client(request):
    workers = User.objects.all()
    workers_count = workers.count()
    inward_count = Inward.objects.all().count()
    dispatchs_count = Dispatch.objects.all().count()
    item = Client.objects.all()

    if request.method =='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            worker_name = form.cleaned_data.get('name')
            messages.success(request, f'{worker_name} has been added')
            return redirect('dashboard-client')
    else:
        form = ClientForm()
    context = {
        'item': item,
        'form': form,
        'workers': workers,
        'workers_count': workers_count,
        'dispatchs_count': dispatchs_count,
        'inward_count': inward_count,
    }
    return render(request, 'dashboard/client.html', context)

@login_required
def inward(request):
    items = Inward.objects.all()
    inward_count = items.count()
    workers_count = User.objects.all().count()
    dispatchs_count = Dispatch.objects.all().count()
    #items = Inward.objects.raw
    if request.method =='POST':
        form = InwardForm(request.POST)
        if form.is_valid():
            form.save()
            inward_name = form.cleaned_data.get('name')
            messages.success(request, f'{inward_name} has been added')
            return redirect('dashboard-inward')
    else:
        form = InwardForm()
    context = {
        'items': items,
        'form': form,
        'workers_count': workers_count,
        'dispatchs_count': dispatchs_count,
        'inward_count': inward_count
    }
    return render(request, 'dashboard/inward.html',context)

@login_required
def inward_delete(request, pk):
    item = Inward.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-inward')
    return render(request, 'dashboard/inward_delete.html')

@login_required
def inward_update(request, pk):
    item = Inward.objects.get(id=pk)
    if request.method == 'POST':
        form = InwardForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-inward')
    else:
        form = InwardForm(instance=item)
    context = {
        'form': form,

    }
    return render(request, 'dashboard/inward_update.html', context)

@login_required
def dispatch(request):
    dispatchs = Dispatch.objects.all()
    dispatchs_count = dispatchs.all().count()
    workers_count = User.objects.all().count()
    inward_count = Inward.objects.all().count()
    
   
    context = {
        'dispatchs': dispatchs,
        'workers_count': workers_count,
        'dispatchs_count': dispatchs_count,
        'inward_count': inward_count,
        
    }
    return render(request, 'dashboard/dispatch.html', context)


class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        #getting the template
        pdf = render_to_pdf('invoice.html')
         
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response



