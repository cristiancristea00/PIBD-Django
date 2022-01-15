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
            judecator.cnp = self.request.POST.get('CNP_add')
            judecator.nume = self.request.POST.get('Nume_add').upper()
            judecator.prenume = self.request.POST.get('Prenume_add')
            judecator.telefon = self.request.POST.get('Telefon_add')
            judecator.email = self.request.POST.get('Email_add')
            judecator.specializare = self.request.POST.get('Specializare_add')
            judecator.preluare_mandat = parse(self.request.POST.get('Preluare_mandat_add'))
            judecator.expirare_mandat = parse(self.request.POST.get('Expirare_mandat_add'))
            judecator.create()

        elif self.request.POST.get('addProces') is not None:

            proces = Proces()
            proces.numar = self.request.POST.get('Numar_add')
            proces.obiect = self.request.POST.get('Obiect_add')
            proces.materie_juridica = self.request.POST.get('Materie_juridica_add')
            proces.stadiu_procesual = self.request.POST.get('Stadiu_procesual_add')
            proces.reclamant = self.request.POST.get('Reclamant_add')
            proces.parat = self.request.POST.get('Parat_add')
            proces.create()

        elif self.request.POST.get('addProgramare') is not None:

            with transaction.atomic():
                judecator = Judecator.objects.get(id_judecator=int(self.request.POST.get('ID_Judecator_add')))
                proces = Proces.objects.get(id_proces=int(self.request.POST.get('ID_Proces_add')))

            programare = Programare()
            programare.judecator = judecator
            programare.proces = proces
            programare.oras = self.request.POST.get('Oras_add')
            programare.locatie = self.request.POST.get('Locatie_add')
            programare.sala = self.request.POST.get('Sala_add')
            programare.data = parse(self.request.POST.get('Data_add'))
            programare.ora = parse(self.request.POST.get('Ora_add'))
            programare.create()

        return self.render_to_response(self.get_context_data())
