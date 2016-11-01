from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.


#class IndexView(TemplateView):
#    template_name = 'index.html'
#
#    def get_context_data(self, **kwargs):
#        context = super(IndexView, self).get_context_data(**kwargs)
#        return context


def index(request):
    return render(request, 'index.html', {})
