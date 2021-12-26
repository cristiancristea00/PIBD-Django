from django.views.generic import TemplateView


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'


class JudecatoriPageView(TemplateView):
    template_name = 'judecatori.html'


class ProcesePageView(TemplateView):
    template_name = 'procese.html'


class ProgramariPageView(TemplateView):
    template_name = 'programari.html'
