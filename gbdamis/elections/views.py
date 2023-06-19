import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from gbdamis.elections.models import Position, Nomination
from .forms import PositionForm
# Create your views here.
log = logging.getLogger(__name__)

def nomination(request):
    form = PositionForm(request.POST or None)

    if form.is_valid():
        form.save()
   
    


def delete_position(request, pk):
    position = get_object_or_404(Position, pk=pk)
    position.delete()
    messages.success(request, 'Position deleted successfully')
    return redirect('admin-nominations')

def delete_nomination(request, pk ):
    nomination = get_object_or_404(Nomination, pk=pk)
    nomination.delete()
    messages.success(request, 'Nomination deleted successfully')
    return redirect('admin-nominations')


def approve_nomination(request, pk):
    nomination =  get_object_or_404(Nomination, pk=pk)
    nomination.approved = True
    nomination.save()
    messages.success(request, 'Nomination approved succesfully')
    return redirect('admin-nominations')

def decline_nomination(request, pk):
    nomination =  get_object_or_404(Nomination, pk=pk)
    nomination.declined = True
    nomination.save()
    messages.success(request, 'Nomination declined succesfully')
    return redirect('admin-nominations')
