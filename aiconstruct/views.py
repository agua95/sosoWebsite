# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db import transaction
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.utils.decorators import method_decorator
from django.conf import settings
from datetime import datetime, date


class ConstructHomeView(TemplateView):
    template_name = 'aiconstruct/home.html'