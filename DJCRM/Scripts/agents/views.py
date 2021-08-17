from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.shortcuts import reverse
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin
from django.core.mail import send_mail
import random
# Create your views here.
class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agents_list.html'

    def get_queryset(self):
        request_user_userprofile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_userprofile)

class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agents_create.html'
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agents-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(str(random.randint(0, 1000000)))
        user.save()
        Agent.objects.create(
            user=user,
            organisation = self.request.user.userprofile

        )
        send_mail(
            subject = "You are invited to be an Agent",
            message = "You were added as an Agent on DJCRM. Please come login to start working",
            from_email = "admin@test.com",
            recipient_list = [user.email]
        )
        # agent.organisation = self.request.user.userprofile
        # agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agents_detail.html'
    context_object_name = 'agent'
    def get_queryset(self):
        request_user_userprofile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_userprofile)

class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agents_update.html'
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agents-list")

    def get_queryset(self):
        request_user_userprofile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_userprofile)

class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agents_delete.html'
    context_object_name = 'agent'

    def get_success_url(self) -> str:
        return reverse("agents:agents-list")

    def get_queryset(self):
        request_user_userprofile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_userprofile)