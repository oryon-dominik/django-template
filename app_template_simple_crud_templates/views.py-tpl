from django.urls import reverse_lazy
from django.views import generic

from .models import {{ camel_case_app_name }}


class {{ camel_case_app_name }}Index(generic.TemplateView):
    template_name = "{{ app_name }}s/index.html.djt"
    extra_context = {"{{ app_name }}s_title": "{{ camel_case_app_name }} Application"}


class {{ camel_case_app_name }}List(generic.ListView):
    model = {{ camel_case_app_name }}
    template_name = "{{ app_name }}s/list.html.djt"
    context_object_name = "{{ app_name }}s"


class {{ camel_case_app_name }}Detail(generic.DetailView):
    model = {{ camel_case_app_name }}
    template_name = "{{ app_name }}s/detail.html.djt"
    context_object_name = "{{ app_name }}"


class {{ camel_case_app_name }}Create(generic.CreateView):
    model = {{ camel_case_app_name }}
    template_name = '{{ app_name }}s/create.html.djt'
    success_url = reverse_lazy("{{ app_name }}s:list")
    fields = ['name', 'description', 'state']


class {{ camel_case_app_name }}Update(generic.UpdateView):
    model = {{ camel_case_app_name }}
    template_name = "{{ app_name }}s/update.html.djt"
    context_object_name = "{{ app_name }}"
    success_url = reverse_lazy('{{ app_name }}s:list')
    fields = ['name', 'description', 'state']


class {{ camel_case_app_name }}Delete(generic.DeleteView):
    model = {{ camel_case_app_name }}
    template_name = "{{ app_name }}s/confirm-delete.html.djt"
    context_object_name = "{{ app_name }}"
    success_url = reverse_lazy('{{ app_name }}s:list')
