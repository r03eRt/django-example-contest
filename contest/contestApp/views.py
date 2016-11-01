from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# For generic view
from django.views.generic import TemplateView

from .models import Vote

# Index Function view
#def index(request):
#    return render(request, 'index.html', {})



# Index class based view
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # Pasar por contexto
        #context['books'] = 'hola'
        #context['num'] = Vote.objects.filter(email='mivoto@gmail.com').count()
        return context


# Index class based view
class Pagina2View(TemplateView):
    template_name = 'pagina2.html'


# Index class based view
class Pagina3View(TemplateView):
    template_name = 'pagina3.html'


# Index class based view
class Pagina4View(TemplateView):
    template_name = 'pagina4.html'
