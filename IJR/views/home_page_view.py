from dateutil.parser import parse
from django.db import transaction
from django.views.generic import TemplateView

from IJR.models import Judecator, Proces, Programare


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            procese = Proces.objects.all()
            judecatori = Judecator.objects.all()
        context['procese'] = procese
        context['judecatori'] = judecatori
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('addJudecator', None) is not None:

            judecator = Judecator()
            judecator.cnp = self.request.POST.get('CNP_add', None)
            judecator.nume = self.request.POST.get('Nume_add', None).upper()
            judecator.prenume = self.request.POST.get('Prenume_add', None)
            judecator.telefon = self.request.POST.get('Telefon_add', None)
            judecator.email = self.request.POST.get('Email_add', None)
            judecator.specializare = self.request.POST.get('Specializare_add', None)
            judecator.preluare_mandat = parse(self.request.POST.get('Preluare_mandat_add', None))
            judecator.expirare_mandat = parse(self.request.POST.get('Expirare_mandat_add', None))
            judecator.create()

        elif self.request.POST.get('addProces', None) is not None:

            proces = Proces()
            proces.numar = self.request.POST.get('Numar_add', None)
            proces.obiect = self.request.POST.get('Obiect_add', None)
            proces.materie_juridica = self.request.POST.get('Materie_juridica_add', None)
            proces.stadiu_procesual = self.request.POST.get('Stadiu_procesual_add', None)
            proces.reclamant = self.request.POST.get('Reclamant_add', None)
            proces.parat = self.request.POST.get('Parat_add', None)
            proces.create()

        elif self.request.POST.get('addProgramare', None) is not None:

            with transaction.atomic():
                judecator = Judecator.objects.get(id_judecator=int(self.request.POST.get('ID_Judecator_add', None)))
                proces = Proces.objects.get(id_proces=int(self.request.POST.get('ID_Proces_add', None)))

            programare = Programare()
            programare.judecator = judecator
            programare.proces = proces
            programare.oras = self.request.POST.get('Oras_add', None)
            programare.locatie = self.request.POST.get('Locatie_add', None)
            programare.sala = self.request.POST.get('Sala_add', None)
            programare.data = parse(self.request.POST.get('Data_add', None))
            programare.ora = parse(self.request.POST.get('Ora_add', None))
            programare.create()

        return self.render_to_response(self.get_context_data())
