from dateutil.parser import parse
from django.db import transaction
from django.views.generic import TemplateView

from IJR.models import Judecator


class JudecatoriPageView(TemplateView):
    template_name = 'judecatori.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            judecatori = Judecator.objects.all()
        context['judecatori'] = judecatori
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('updateJudecator') is not None:

            with transaction.atomic():
                judecator = Judecator.objects.get(
                    id_judecator=int(self.request.POST.get('Select_judecator_Update')))

            cnp = self.request.POST.get('CNP_update')
            cnp = cnp if cnp != '' else judecator.cnp
            nume = self.request.POST.get('Nume_update')
            nume = nume.upper() if nume != '' else judecator.nume
            prenume = self.request.POST.get('Prenume_update')
            prenume = prenume if prenume != '' else judecator.prenume
            telefon = self.request.POST.get('Telefon_update')
            telefon = telefon if telefon != '' else judecator.telefon
            email = self.request.POST.get('Email_update')
            email = email if email != '' else judecator.email
            specializare = self.request.POST.get('Specializare_update')
            specializare = specializare if specializare != '' else judecator.specializare
            preluare_mandat = self.request.POST.get('Preluare_mandat_update')
            preluare_mandat = parse(preluare_mandat) if preluare_mandat != '' else judecator.preluare_mandat
            expirare_mandat = self.request.POST.get('Expirare_mandat_update')
            expirare_mandat = parse(expirare_mandat) if expirare_mandat != '' else judecator.expirare_mandat

            judecator = Judecator(id_judecator=judecator.id_judecator, cnp=cnp, nume=nume, prenume=prenume,
                                  telefon=telefon, email=email, specializare=specializare,
                                  preluare_mandat=preluare_mandat, expirare_mandat=expirare_mandat)

            judecator.update()

        elif self.request.POST.get('deleteJudecator') is not None:

            with transaction.atomic():
                judecator = Judecator.objects.get(
                    id_judecator=int(self.request.POST.get('Select_judecator_Delete')))

            judecator.remove()

        return self.render_to_response(self.get_context_data())
