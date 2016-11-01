from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# For generic view
from django.views.generic import TemplateView, FormView

from .models import Vote

# Form forms
from .forms import PictureForm, VoteForm
from django.http import HttpResponseRedirect

# Index Function view
#def index(request):
#    return render(request, 'index.html', {})



# Index class based view
class IndexView(TemplateView):
    template_name = 'index.html'

    # Context data
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # Pasar por contexto
        #context['books'] = 'hola'
        #context['num'] = Vote.objects.filter(email='mivoto@gmail.com').count()
        return context

# Index class based view
class Pagina2View(FormView):
    template_name = 'pagina2.html'
    form_class = VoteForm
    success_url = "/pagina2/"

    def form_valid(self, form):
        print(self.request.POST['email'])
        vote = form.save(commit=False)
        # Validatiosn here
        vote.save()
        return super(Pagina2View, self).form_valid(form)



# Index class based view
class Pagina3View(TemplateView):
    template_name = 'pagina3.html'


# Index class based view
class Pagina4View(TemplateView):
    template_name = 'pagina4.html'
