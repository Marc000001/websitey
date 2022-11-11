from datetime import datetime

from django.shortcuts import render, redirect, reverse

from accounts.filters import Filter
from .models import Patient, Note
# Create your views here.
from django.views.generic import ListView, DetailView
from .forms import PatientForm, NoteForm


def delete_note(request, pk):
    # print(pk)
    note = Note.objects.filter(patient=pk)
    # print(note.values())

    qs2 = Note.objects.get(id=pk)
    qs = Note.objects.filter(id=qs2.id)
    qs.delete()
    patient_id = qs2.patient_id
    # note.delete()
    return redirect(reverse('detailed', args=[patient_id]))


def add_note(request, pk):
    patient = Patient.objects.get(id=pk)
    patient_id = patient.id
    form = NoteForm(instance=patient)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=patient)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['note'];

        c = Note(patient=patient, created_by=name, note=body, date_created=datetime.now())
        c.save()

        return redirect(reverse('detailed', args=[patient_id]))
    else:

        form = NoteForm()

    context = {
        'form': form
    }

    return render(request, 'add_note.html', context)


def result(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query:
            user = request.user.level
            patient = Patient.objects.filter(name__contains=query, level=user)
            return render(request, 'result.html', {'patient': patient})

        else:
            print("Such Patient does not exist")
            return request(request, 'result.html', {})


def deletePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect('patient_list')


def updatePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    patient_id = patient.id
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)

        if form.is_valid():
            form.save()
            return redirect(reverse('detailed', args=[patient_id]))
    context = {
        "form": form
    }

    return render(request, 'updatePatient.html', context)


def addPatient(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()


            return redirect('patient_list')

    context = {
        "form": form
    }

    return render(request, 'addPatient.html', context)


class PatientListView(ListView):
    queryset = Patient.objects.all()
    template_name = "list.html"


class PatientDetailView(DetailView):
    queryset = Patient.objects.all()
    template_name = "detail.html"


def list_patient(request):
    user = request.user.level
    patient = Patient.objects.filter(level=user)
    myFilter = Filter(request.GET, queryset=patient)
    patient = myFilter.qs

    print(user)
    context = {
        'patient': patient,
        'myFilter': myFilter,
    }
    return render(request, 'list.html', context)


def list_ward(request):
    user = request.user.level
    userward = request.user.ward
    patient = Patient.objects.filter(level=user, ward=userward)
    myFilter = Filter(request.GET, queryset=patient)
    patient = myFilter.qs

    print(user)
    context = {
        'patient': patient,
        'myFilter': myFilter,
    }
    return render(request, 'wardlist.html', context)
