from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .forms import TreePictureForm
from .models import TreePicture

class TreePictureList(ListView):
    model = TreePicture
    template_name = 'TreePicturesApp/TreePictureList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TreePictureDetail(DetailView):
    model = TreePicture
    template_name = 'TreePicturesApp/TreePicture_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class TreePictureFormView(View):
    form_class = TreePictureForm
    initial    = {'key': 'value'}
    template_name = 'TreePicturesApp/TreePictureFormTemplate.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pictures:picture_form'))
        return render(request, self.template_name, {'form': form})

# Create your views here.
