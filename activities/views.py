from django.shortcuts import render, redirect, get_object_or_404
from .models import Extracurricular, Subject
from .forms import TypeForm, SubjectForm, YearForm, CostForm, EffortForm

def index(request):
    if 'type' not in request.session:
        return redirect('type_step')
    if request.session['type'] == 'Summer Program' or request.session['type'] == 'Competition':
        if 'subjects' not in request.session:
            return redirect('subject_step')
        if 'year' not in request.session:
            return redirect('year_step')
        if 'cost' not in request.session:
            return redirect('cost_step')
    elif request.session['type'] == 'Scholarship':
        if 'year' not in request.session:
            return redirect('year_step')
        if 'effort' not in request.session:
            return redirect('effort_step')

    extracurriculars = Extracurricular.objects.all()
    if 'subjects' in request.session:
        extracurriculars = extracurriculars.filter(subject__in=request.session['subjects'])
    if 'year' in request.session:
        extracurriculars = extracurriculars.filter(year=request.session['year'])
    if 'cost' in request.session:
        extracurriculars = extracurriculars.filter(cost=request.session['cost'])
    if 'effort' in request.session:
        extracurriculars = extracurriculars.filter(effort=request.session['effort'])
    if 'type' in request.session:
        extracurriculars = extracurriculars.filter(type=request.session['type'])

    return render(request, 'activities/index.html', {'extracurriculars': extracurriculars})

def type_step(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            request.session['type'] = form.cleaned_data.get('extracurricular_type')
            return redirect('index')
    else:
        form = TypeForm()
    return render(request, 'activities/type_step.html', {'form': form})

def subject_step(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subjects = form.cleaned_data.get('subjects')
            request.session['subjects'] = [subject.id for subject in subjects]
            return redirect('index')
    else:
        form = SubjectForm()
    return render(request, 'activities/subject_step.html', {'form': form})

def year_step(request):
    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            request.session['year'] = form.cleaned_data.get('year')
            return redirect('index')
    else:
        form = YearForm()
    return render(request, 'activities/year_step.html', {'form': form})

def cost_step(request):
    if request.method == 'POST':
        form = CostForm(request.POST)
        if form.is_valid():
            request.session['cost'] = form.cleaned_data.get('cost')
            return redirect('index')
    else:
        form = CostForm()
    return render(request, 'activities/cost_step.html', {'form': form})

def effort_step(request):
    if request.method == 'POST':
        form = EffortForm(request.POST)
        if form.is_valid():
            request.session['effort'] = form.cleaned_data.get('effort')
            return redirect('index')
    else:
        form = EffortForm()
    return render(request, 'activities/effort_step.html', {'form': form})

def extracurricular_detail(request, extracurricular_id):
    extracurricular = get_object_or_404(Extracurricular, id=extracurricular_id)
    return render(request, 'activities/detail.html', {'extracurricular': extracurricular})