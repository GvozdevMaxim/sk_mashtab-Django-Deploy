from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from core.models import Project


class HomeView(ListView):
    model = Project
    template_name = 'core/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all()


class DetailProjectView(DetailView):
    model = Project
    template_name = 'core/project-details.html'
    context_object_name = 'project'

    def get_object(self, queryset=None):
        return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project = context['project']

        prev_project = Project.objects.filter(pk__lt=project.pk).order_by('-pk').first()
        next_project = Project.objects.filter(pk__gt=project.pk).order_by('pk').first()

        context['prev_project'] = prev_project
        context['next_project'] = next_project

        return context


class ConfidenceView(TemplateView):
    template_name = 'core/confidence.html'
