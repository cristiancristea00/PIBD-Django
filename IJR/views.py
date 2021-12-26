from dateutil.parser import parse
from django.views.generic import TemplateView

from IJR.models import *


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        procese = Proces.objects.all()
        judecatori = Judecator.objects.all()
        context['procese'] = procese
        context['judecatori'] = judecatori
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('addJudecator', None) is not None:

            judecator = Judecator()
            judecator.cnp = self.request.POST.get('CNP_add', None)
            judecator.nume = self.request.POST.get('Nume_add', None)
            judecator.prenume = self.request.POST.get('Prenume_add', None)
            judecator.telefon = self.request.POST.get('Telefon_add', None)
            judecator.email = self.request.POST.get('Email_add', None)
            judecator.specializare = self.request.POST.get('Specializare_add', None)
            judecator.preluare_mandat = parse(self.request.POST.get('Preluare_mandat_add', None))
            judecator.expirare_mandat = parse(self.request.POST.get('Expirare_mandat_add', None))
            judecator.save(force_insert=True)

        elif self.request.POST.get('addProces', None) is not None:

            proces = Proces()
            proces.numar = self.request.POST.get('Numar_add', None)
            proces.obiect = self.request.POST.get('Obiect_add', None)
            proces.materie_juridica = self.request.POST.get('Materie_juridica_add', None)
            proces.stadiu_procesual = self.request.POST.get('Stadiu_procesual_add', None)
            proces.reclamant = self.request.POST.get('Reclamant_add', None)
            proces.parat = self.request.POST.get('Parat_add', None)
            proces.save(force_insert=True)

        elif self.request.POST.get('addProgramare', None) is not None:

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
            programare.save(force_insert=True)

        return self.render_to_response(self.get_context_data())


class JudecatoriPageView(TemplateView):
    template_name = 'judecatori.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        judecatori = Judecator.objects.all()
        context['judecatori'] = judecatori
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('updateJudecator', None) is not None:

            judecator = Judecator.objects.get(id_judecator=int(self.request.POST.get('Select_judecator_Update', None)))
            cnp = self.request.POST.get('CNP_update', None)
            cnp = cnp if cnp != '' else judecator.cnp
            nume = self.request.POST.get('Nume_update', None)
            nume = nume if nume != '' else judecator.nume
            prenume = self.request.POST.get('Prenume_update', None)
            prenume = prenume if prenume != '' else judecator.prenume
            telefon = self.request.POST.get('Telefon_update', None)
            telefon = telefon if telefon != '' else judecator.telefon
            email = self.request.POST.get('Email_update', None)
            email = email if email != '' else judecator.email
            specializare = self.request.POST.get('Specializare_update', None)
            specializare = specializare if specializare != '' else judecator.specializare
            preluare_mandat = self.request.POST.get('Preluare_mandat_update', None)
            preluare_mandat = parse(preluare_mandat) if preluare_mandat != '' else judecator.preluare_mandat
            expirare_mandat = self.request.POST.get('Expirare_mandat_update', None)
            expirare_mandat = parse(expirare_mandat) if expirare_mandat != '' else judecator.expirare_mandat

            judecator = Judecator(id_judecator=judecator.id_judecator, cnp=cnp, nume=nume, prenume=prenume, telefon=telefon, email=email,
                                  specializare=specializare, preluare_mandat=preluare_mandat, expirare_mandat=expirare_mandat)

            judecator.save(force_update=True)

        elif self.request.POST.get('deleteJudecator', None) is not None:

            judecator = Judecator.objects.get(id_judecator=int(self.request.POST.get('Select_judecator_Delete', None)))
            judecator.delete()

        return self.render_to_response(self.get_context_data())


class ProcesePageView(TemplateView):
    template_name = 'procese.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        procese = Proces.objects.all()
        context['procese'] = procese
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('updateProces', None) is not None:

            proces = Proces.objects.get(id_proces=int(self.request.POST.get('Select_proces_Update', None)))
            numar = self.request.POST.get('Numar_update', None)
            numar = numar if numar != '' else proces.numar
            obiect = self.request.POST.get('Obiect_update', None)
            obiect = obiect if obiect != '' else proces.obiect
            materie_juridica = self.request.POST.get('Materie_juridica_update', None)
            materie_juridica = materie_juridica if materie_juridica != '' else proces.materie_juridica
            stadiu_procesual = self.request.POST.get('Stadiu_procesual_update', None)
            stadiu_procesual = stadiu_procesual if stadiu_procesual != '' else proces.stadiu_procesual
            reclamant = self.request.POST.get('Reclamant_update', None)
            reclamant = reclamant if reclamant != '' else proces.reclamant
            parat = self.request.POST.get('Parat_update', None)
            parat = parat if parat != '' else proces.parat

            proces = Proces(id_proces=proces.id_proces, numar=numar, obiect=obiect, materie_juridica=materie_juridica,
                            stadiu_procesual=stadiu_procesual, reclamant=reclamant, parat=parat)

            proces.save(force_update=True)

        elif self.request.POST.get('deleteProces', None) is not None:

            proces = Proces.objects.get(id_proces=int(self.request.POST.get('Select_proces_Delete', None)))
            proces.delete()

        return self.render_to_response(self.get_context_data())


class ProgramariPageView(TemplateView):
    template_name = 'programari.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        programari = Programare.objects.all()
        context['programari'] = programari
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('updateProgramare', None) is not None:

            programare = Programare.objects.get(id_programare=int(self.request.POST.get('Select_programare_Update', None)))
            judecator = programare.judecator
            proces = programare.proces
            oras = self.request.POST.get('Oras_update', None)
            oras = oras if oras != '' else programare.oras
            locatie = self.request.POST.get('Locatie_update', None)
            locatie = locatie if locatie != '' else programare.locatie
            data = self.request.POST.get('Data_update', None)
            data = parse(data) if data != '' else programare.data
            ora = self.request.POST.get('Ora_update', None)
            ora = parse(ora) if ora != '' else programare.ora

            programare = Programare(id_programare=programare.id_programare, judecator=judecator, proces=proces, oras=oras, locatie=locatie, data=data,
                                    ora=ora)

            programare.save(force_update=True)

        elif self.request.POST.get('deleteProgramare', None) is not None:

            programare = Programare.objects.get(id_programare=int(self.request.POST.get('Select_programare_Delete', None)))
            programare.delete()

        return self.render_to_response(self.get_context_data())
