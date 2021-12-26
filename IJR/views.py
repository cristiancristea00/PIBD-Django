from django.views.generic import TemplateView


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        from IJR.models import Proces
        from IJR.models import Judecator

        context = super().get_context_data(**kwargs)
        procese = Proces.objects.all()
        judecatori = Judecator.objects.all()
        context['procese'] = procese
        context['judecatori'] = judecatori
        return context


class JudecatoriPageView(TemplateView):
    template_name = 'judecatori.html'

    def get_context_data(self, **kwargs):
        from IJR.models import Judecator

        context = super().get_context_data(**kwargs)
        judecatori = Judecator.objects.all()
        context['judecatori'] = judecatori
        return context


class ProcesePageView(TemplateView):
    template_name = 'procese.html'

    def get_context_data(self, **kwargs):
        from IJR.models import Proces

        context = super().get_context_data(**kwargs)
        procese = Proces.objects.all()
        context['procese'] = procese
        return context


class ProgramariPageView(TemplateView):
    template_name = 'programari.html'

    def get_context_data(self, **kwargs):
        from IJR.models import Programare

        context = super().get_context_data(**kwargs)
        programari = Programare.objects.all()
        context['programari'] = programari
        return context
