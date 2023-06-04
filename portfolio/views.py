from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from config.settings.common import THE_SITE_NAME
from . import models


class ProjectCreateView(CreateView):
    """
    Create view for models.Project model.
    """
    model = models.Project
    fields = "__all__"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Project"
        context["the_site_name"] = THE_SITE_NAME
        return context


class ProjectUpdateView(UpdateView):
    """
    Update view for models.Project model.
    """
    model = models.Project
    fields = "__all__"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Project"
        context["the_site_name"] = THE_SITE_NAME
        return context


class ProjectDetailView(DetailView):
    """
    Detail view for models.Project model.
    """
    model = models.Project
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        return context


class ProjectListView(ListView):
    """
    List view for models.Project model.
    """
    queryset = models.Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Projects"
        context["the_site_name"] = THE_SITE_NAME
        return context


